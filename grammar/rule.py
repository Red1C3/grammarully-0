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

    def matched_windows(self, sentence: Sentence):
        tagged = sentence.get_bnc_tagged()
        matches = []
        for i in range(len(tagged) - self.con_len + 1):
            sub_tagged = tagged[i:self.con_len + i]
            # TODO take all possible POS tags into account
            sub_tagged = [x[0] if self.construct[i] == 'w' else x[1][0] for i, x in enumerate(sub_tagged)]
            sub_tagged_str = str.join(' ', sub_tagged)
            if re.match(Rule.pattern_re_string(self.incorrect_pattern), sub_tagged_str):
                matches.append(i)
        return matches

    def first_matched_window(self,sentence:Sentence):
        tagged = sentence.get_bnc_tagged()
        con_len = len(self.construct)
        for i in range(len(tagged) - con_len + 1):
            sub_tagged = tagged[i:con_len + i]
            # TODO take all possible POS tags into account
            sub_tagged = [x[0] if self.construct[i] == 'w' else x[1][0] for i, x in enumerate(sub_tagged)]
            sub_tagged_str = str.join(' ', sub_tagged)
            if re.match(Rule.pattern_re_string(self.incorrect_pattern), sub_tagged_str):
                return i
        return -1

    #TODO handle case where cannot correct
    def correct_window(self,sentence:Sentence,i:int):
        tagged=sentence.get_bnc_tagged()[i:i+self.con_len]
        correct=[]
        for d in self.correction_dict:
            if 'idx' in d:
                word = tagged[d['idx']][0]
            if 'const' in d:
                word = d['const']
            if 'pronoun_idx' in d and 'tense' in d:
                tense = d['tense']
                pronoun = tagged[d['pronoun_idx']][0]
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
            elif 'tense' in d:
                word = conjugate(verb=word, tense=d['tense'])
            correct.append(word)
        return str.join(' ', correct)

    def __str__(self):
        return self.pattern_re_string(self.construct)+" : "+self.pattern_re_string(self.incorrect_pattern) + "-->" + str(self.correction_dict)
