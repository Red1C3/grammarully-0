import re
from language.sentence import Sentence

class Rule:
    #construct: an array of either w or p values, indicating words or POS options
    #pattern: an array of possible choices for each construct
    # example:
    # construct: [w,p,w]
    # pattern: [(and,no),(NN0,NN1),(meow,cat)]
    def __init__(self, incorrect_construct, incorrect_pattern,correct_pattern=None,hint=None):
        self.construct=incorrect_construct
        self.incorrect_pattern=incorrect_pattern
        self.correct_pattern=correct_pattern
        self.hint=hint

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
        return str.join(' ',string)

    # Matches range is (inclusive,exclusive)
    def matched_windows(self, sentence: Sentence):
        tagged = sentence.get_bnc_tagged()
        con_len = len(self.construct)
        matches = []
        for i in range(len(tagged) - con_len + 1):
            sub_tagged = tagged[i:con_len + i]
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
