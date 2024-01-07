import re

from pattern.text import SINGULAR, PLURAL

from language.sentence import Sentence
from pattern.text.en import conjugate

# TODO when adding verbs tense changing, add v-type to the construct which replaces the verb with all its
# tenses
class Rule:
    #construct: an array of either w or p values, indicating words or POS options
    #pattern: an array of possible choices for each construct
    # example:
    # construct: [w,p,w]
    # pattern: [(and,no),(NN0,NN1),(meow,cat)]
    def __init__(self, incorrect_construct, incorrect_pattern, correction_dict: (tuple | None) = None, hint=None):
        self.construct=incorrect_construct
        self.incorrect_pattern=incorrect_pattern
        self.correction_dict=correction_dict
        self.hint=hint

        self.con_len=len(incorrect_construct)

    @staticmethod
    def pattern_re_string(pattern):
        string=[]
        for group in pattern:
            if type(group) is tuple:
                joined_group=str.join("|",group)
                joined_group='('+joined_group+')'
            else:
                joined_group=group
            string.append(joined_group)
        return '^'+str.join(' ',string)+'$'

    @staticmethod
    def negative(*args):
        string =  str.join("|",args)
        return f'(?!{string}).*'

    def first_matched_window(self,sentence:Sentence):
        all_tagged = sentence.get_bnc_tagged()
        for poss, tagged in enumerate(all_tagged):
            tagged = list(tagged)
            con_len = len(self.construct)
            if 'b' in self.construct:
                for i in range(len(tagged)):
                    cur_const = 0
                    sub_tagged = tagged[i:]
                    baked_sub_tagged = []
                    for comp in sub_tagged:
                        if cur_const == len(self.construct):
                            baked_sub_tagged_str = str.join(' ', baked_sub_tagged)
                            if re.match(Rule.pattern_re_string(self.incorrect_pattern), baked_sub_tagged_str):
                                return i, len(baked_sub_tagged), poss
                            else:
                                break
                        if self.construct[cur_const] == 'w':
                            baked_sub_tagged.append(comp[0])
                            cur_const += 1
                        elif self.construct[cur_const] == 'p':
                            baked_sub_tagged.append(comp[1][0])
                            cur_const += 1
                        elif self.construct[cur_const] == 'b':
                            baked_sub_tagged.append(comp[0])
                            lookup_const = self.incorrect_pattern[cur_const + 1]
                            if (self.construct[cur_const + 1] == 'w' and comp[0] in lookup_const ) or \
                                    (self.construct[cur_const + 1] == 'p' and comp[1][0] in lookup_const):
                                cur_const += 2

            else:
                for i in range(len(tagged) - con_len + 1):
                    sub_tagged = tagged[i:con_len + i]
                    sub_tagged = [x[0] if self.construct[i] == 'w' else x[1][0] for i, x in enumerate(sub_tagged)]
                    sub_tagged_str = str.join(' ', sub_tagged)
                    if re.match(Rule.pattern_re_string(self.incorrect_pattern), sub_tagged_str):
                        return i, len(sub_tagged), poss
        return -1, 0, 0

    #TODO handle case where cannot correct
    def correct_window(self, sentence: Sentence, i: int, window_len: int, possibility: int):
        tagged = sentence.get_bnc_tagged()[possibility][i:i + window_len]
        correct=[]
        for d in self.correction_dict:
            if 'idx' in d:
                word = tagged[d['idx']][0]
                if 'until_word' in d:
                    word = [word]
                    until = d['until_word']
                    idx = d['idx'] + 1
                    if type(until) is tuple:
                        while tagged[idx][0] not in until:
                            word.append(tagged[idx][0])
                            idx += 1
                    elif type(until) is int:
                        until_words = self.incorrect_pattern[until]
                        while tagged[idx][0] not in until_words:
                            word.append(tagged[idx][0])
                            idx += 1
                    else:
                        while tagged[idx][0] != until:
                            word.append(tagged[idx][0])
                            idx += 1
                    word = str.join(' ', word)

            if 'const' in d:
                word = d['const']
            if 'pronoun_idx' in d and 'tense' in d:
                tense = d['tense']
                pronoun = tagged[d['pronoun_idx']][0].lower()
                if pronoun == 'i':
                    word = conjugate(verb=word, person=1, number=SINGULAR, tense=tense)
                elif pronoun in ['he', 'she', 'it']:
                    word = conjugate(verb=word, person=3, number=SINGULAR, tense=tense)
                elif pronoun == 'they':
                    word = conjugate(verb=word, person=3, number=PLURAL, tense=tense)
                elif pronoun == 'we':
                    word = conjugate(verb=word, person=1, number=PLURAL, tense=tense)
                elif pronoun == 'you':
                    word = conjugate(verb=word, perons=2, number=PLURAL, tense=tense)  # I know it can be singular
                else:
                    word = conjugate(verb=word, person=3, number=SINGULAR, tense=tense)
            elif 'number' in d and 'tense' in d:
                word = conjugate(verb=word, person=3, number=d['number'], tense=d['tense'])
            elif 'tense' in d:
                word = conjugate(verb=word, tense=d['tense'])
            correct.append(word)
        return str.join(' ', correct)

    def __str__(self):
        return self.pattern_re_string(self.construct)[1:-1]+" : "+self.pattern_re_string(self.incorrect_pattern)[1:-1] + "-->" + str(self.correction_dict)
