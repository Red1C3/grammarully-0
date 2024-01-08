from grammar.rule import Rule
from language.sentence import Sentence
from pattern.text.en import PAST, PRESENT, INFINITIVE, PARTICIPLE
from pattern.text.en import PLURAL

class Checker:
    def __init__(self, *args):
        if len(args) != 0:
            self.rules = args[0]
        else:
            self.rules = []
        self.initRules()

    def initRules(self):
        present_simple_kw = ('never','always','often','usually', 'regularly', 'every.*', 'daily','seldom','normally','generally','sometimes','rarely')
        present_continuous_kw = ('at present','now.*','at this moment','at this time','next','today')

        self.rules.append(
            Rule(['w', 'w', 'p'], ["more", ("a", "an"), 'AJ0'],
                 ({'idx': 1}, {'idx': 0}, {'idx': 2}))
        )  # 4
        self.rules.append(
            Rule(['w', 'w', 'w'], ['think', 'you', ('a', 'an')],
                 ({'idx': 0}, {'idx': 1}, {'const': 'are'}))
        )  # 5
        self.rules.append(
            Rule(['w', 'w'], [('some', 'certain'), 'extend'],
                 ({'idx': 0}, {'const': 'extent'}))
        )  # 6
        self.rules.append(
            Rule(['w', 'w'], ['is', 'were'],
                 ({'idx': 0}, {'const': 'where'}))
        )  # 7
        self.rules.append(
            Rule(['p', 'w'], ['CRD', 'ore'],
                 ({'idx': 0}, {'const': 'or'}))
        )  # 8
        self.rules.append(
            Rule(['w', 'w', 'w'], ['the', 'only', 'on'],
                 ({'idx': 0}, {'idx': 1}, {'const': 'one'}))
        )  # 9
        self.rules.append(
            Rule(['w', 'w'], ['their', ('is', 'are')],
                 ({'const': 'there'}, {'idx': 1}))
        )  # 10
        self.rules.append(
            Rule(['p', 'w', 'w'], ['SENT_START', 'i', ('a', 'an')],
                 ({'idx': 0}, {'idx': 1}, {'const': 'am'}))
        )  # 11
        self.rules.append(
            Rule(['w', 'w'], ['i', 'new'],
                 ({'idx': 0}, {'const': 'knew'}))
        )  # 12
        self.rules.append(
            Rule(['w', 'w', 'w'], ['please', 'not', 'that'],
                 ({'idx': 0}, {'const': 'note'}, {'idx': 2}))
        )  # 13
        self.rules.append(
            Rule(['w', 'p'], ['nut', ('AV0', 'AJ0')],
                 ({'const': 'not'}, {'idx': 1}))
        )  # 14
        self.rules.append(
            Rule(['w', 'w', 'w'], ['and', 'so', 'one'],
                 ({'idx': 0}, {'idx': 1}, {'const': 'on'}))
        )  # 15
        self.rules.append(
            Rule(['w', 'w'], ['through', 'away'],
                 ({'const': 'throw'}, {'idx': 1}))
        )  # 16
        self.rules.append(
            Rule(['w', 'w', 'w'], ['or', 'way', ('it', 'that', 'this')],
                 ({'idx': 0}, {'const': 'was'}, {'idx': 2}))
        )  # 17
        self.rules.append(
            Rule(['p', 'w'], ['AT0', 'responds'],
                 ({'idx': 0}, {'const': 'response'}))
        )  # 18
        self.rules.append(
            Rule(['w', 'w'], [('think', 'know'), 'off'],
                 ({'idx': 0}, {'const': 'of'}))
        )  # 19
        self.rules.append(
            Rule(['w', 'p', 'w'], ['do', 'XX0', 'us'],
                 ({'idx': 0}, {'idx': 1}, {'const': 'use'}))
        )  # 20
        self.rules.append(
            Rule(['p', 'w', 'w'], ['VVB', 'to', 'use'],
                 ({'idx': 0, 'tense': PAST}, {'idx': 1}, {'idx': '2'}))
        )  # 21
        self.rules.append(
            Rule(['w', 'w'], [('i', 'you', 'he', 'she', 'they', 'we'), ('thing', 'things')],
                 ({'idx': 0}, {'const': 'think', 'tense': PRESENT, 'pronoun_idx': 0}))
        )  # 22
        self.rules.append(
            Rule(['w', 'p'], ['were', 'VBB'],
                 ({'const', 'where'}, {'idx': 1}))
        )  # 23
        self.rules.append(
            Rule(['w','p'],['fore','DPS'],
                 ({'const':'for'},{'idx':1}))
        )# 25
        self.rules.append(
            Rule(['w', 'w', 'p'], ['not', 'too', ('SENT_END', 'NN0', 'NN1', 'NN2')],
                 ({'idx': 0}, {'const': 'two'}, {'idx': 2}))
        )  # 26
        self.rules.append(
            Rule(['w', 'p'], ['your', 'VVN'],
                 ({'const': 'you'}, {'const': 'are'}, {'idx': 1}))
        )  # 27
        self.rules.append(
            Rule(['p', 'w'], ['AJC', 'that'],
                 ({'idx': 0}, {'const': 'than'}))
        )  # 28
        self.rules.append(
            Rule(['w', 'p', 'w'], [('less', 'more'), ('AJ0', 'NN1', 'NN0'), 'then'],
                 ({'idx': 0}, {'idx': 1}, {'const': 'than'}))
        )  # 29
        self.rules.append(
            Rule(['p', 'p'], ['AT0', 'AT0'],
                 ({'idx': 0},))
        )  # 30
        self.rules.append(
            Rule(['w', 'p'], ['than', 'SENT_END'],
                 ({'const': 'then'}, {'idx': 1}))
        )  # 31
        self.rules.append(
            Rule(['w', 'w', 'w'], ['of', 'cause', Rule.negative('and', 'to')],
                 ({'idx': 0}, {'const': 'course'}, {'idx': 2}))
        )  # 32
        self.rules.append(
            Rule(['w', 'w', 'p'], ['eager', 'to', ('VM0', 'VVB', 'VVD', 'VVG', 'VVN', 'VVZ')],
                ({'idx': 0}, {'idx': 1}, {'idx': 2, 'tense': INFINITIVE}))
        )  # 33
        self.rules.append(
            Rule(['w', 'p'], ['or', 'SENT_END'],
                 ({'idx': 1},))
        )  # 34
        self.rules.append(
            Rule(['w','w','p'],['a','much','NN1'],
                 ({'idx':1},{'idx':2}))
        ) # 35
        self.rules.append(
            Rule(['w', 'p'], [('more', 'most'), 'AJS'],
                 ({'idx': 1},))
        )  # 36
        self.rules.append(
            Rule(['w', 'w'], ['is', ('should', 'could', 'would')],
                 ({'const': 'it'}, {'idx': 1}))
        )  # 37
        self.rules.append(
            Rule(['p','p','p'],['DT0','AJ0','DT0'],
                 ({'idx':0},{'idx':1}))
        ) # 38+39
        self.rules.append(
            Rule(['w', 'w', 'p'], [Rule.negative('has', 'will', 'must', 'could', 'can', 'should', 'would', 'does', 'did'), ('he','she','it'), ('VVI', 'VVB')],
                 ({'idx': 0}, {'idx': 1}, {'idx': 2, 'tense': PRESENT, 'pronoun_idx': 1}))
        )  # 40
        self.rules.append(
            Rule(['w', 'p'], ['did', ('VVD', 'VVG', 'VVN', 'VVZ')],
                 ({'idx': 0}, {'idx': 1, 'tense': INFINITIVE}))
        )  # 41
        self.rules.append(
            Rule(['p', 'p', 'p'], [Rule.negative('DT0'), 'VM0', ('VVD', 'VVG', 'VVN', 'VVZ')],
                 ({'idx': 0}, {'idx': 1}, {'idx': 2, 'tense': INFINITIVE}))
        )  # 42
        self.rules.append(
            Rule(['p', 'p', 'p'], [('N..', 'PNP'), 'VM0', ('V.D', 'V.G', 'V.N', 'V.Z')],
                 ({'idx': 0}, {'idx': 1}, {'idx': 2, 'tense': INFINITIVE}))
        )  # 43
        self.rules.append(
            Rule(['w', 'p'], [('is', 'was'), ('VVI', 'VVZ')],
                 ({'idx': 0}, {'idx': 1, 'tense': PAST + PARTICIPLE}))
        )  # 44+45
        self.rules.append(
            Rule(['w', 'p', 'w'], ['as', ('AJ0', 'AV0'), ('like', 'than', 'then')],
                 ({'idx': 0}, {'idx': 1}, {'const': 'as'}))
        )  # 46
        self.rules.append(
            Rule(['p', 'w'], [('AT0', 'DT0'), 'from'],
                 ({'idx': 0}, {'const': 'form'}))
        )  # 47
        self.rules.append(
            Rule(['w', 'w'], ['can', 'not'],
                 ({'const': 'cannot'},))
        )  # 48
        self.rules.append(
            Rule(['w', 'w'], [('more', 'less'), ('then', 'as')],
                 ({'idx': 0}, {'const': 'than'}))
        )  # 49
        self.rules.append(
            Rule(['p', 'w'], ['AJC', ('then', 'as')],
                 ({'idx': 0}, {'const': 'than'}))
        )  # 50
        self.rules.append(
            Rule(['w', 'p'], ['its', ('CJC', 'AT0', 'DT0', 'EX0', 'PRF', 'PRP',
                 'VM0', 'POS', 'PNP', 'AV0', 'AVP', 'TO0', 'DTQ',
                                      'PNQ', 'DTQ', 'AVQ', 'VVI', 'VVZ', 'VVG')],
                 ({'const': 'it'}, {'const': 'is'}, {'idx': 1}))
        )  # 51+52+53
        self.rules.append(
            Rule(['w', 'p'], ['no', ('VM0', 'VVI', 'VVD', 'VVN', 'CJC', 'DT0', 'AT0',
                 'EX0', 'PRF', 'PRP', 'NP0', 'AVP', 'DTQ', 'PNQ', 'AVQ')],
                 ({'const': 'now'}, {'idx': 1}))
        )  # 54+55
        self.rules.append(
            Rule(['w', 'w'], ['no', ('were', 'was', 'been', 'be', 'is')],
                 ({'const': 'now'}, {'idx': 1}))
        )  # 56
        self.rules.append(
            Rule(['w', 'b', 'w'], [('does', 'do', 'did'), '.*', 'can'],
                 ({'idx': -1}, {'idx': 1, 'until_word': 'can'}))
        )  # 3
        self.rules.append(
            Rule(['w', 'p'], [('a', 'an', 'one'), 'NN2'],
                 ({'const': 'the'}, {'idx': 1}))
        )  # 1
        self.rules.append(
            Rule(['p', 'p'], ['NN2', 'V.Z'],
                 ({'idx': 0}, {'idx': 1, 'tense': PRESENT, 'number': PLURAL}))
        )  # C1: plural names should not be followed by 3rd singular present
        self.rules.append(
            Rule(['w', 'p'], [('i', 'we', 'they', 'you'), 'V.Z'],
                 ({'idx': 0}, {'idx': 1, 'tense': PRESENT, 'pronoun_idx': 0}))
        )  # C2: 1st and 2nd person pronouns must not be followed by 3rd person verbs
        self.rules.append(
            Rule(['w', 'w', 'p'], [('i','we','you','they'),present_simple_kw, ('VVB','VVD','VVG','VVZ','VVN')],
                 ({'idx': 0}, {'idx': 1}, {'idx':2 ,'tense': PRESENT, 'pronoun_idx': 0}))
        )  # Present Simple 1 PNP
        self.rules.append(
            Rule(['w', 'w', 'p'], [('he', 'she', 'it'),present_simple_kw, ('VVB','VVD','VVG','VVI','VVN')],
                 ({'idx': 0}, {'idx': 1}, {'idx':2 ,'tense': PRESENT, 'pronoun_idx': 0}))
        )  # Present Simple 1 PNP
        self.rules.append(
            Rule(['p', 'w', 'p'], [('NN.','NP0'),present_simple_kw, ('VVB','VVD','VVG','VVI','VVN')],
                 ({'idx': 0}, {'idx': 1}, {'idx':2 ,'tense': PRESENT, 'pronoun_idx': 0}))
        )  # Present Simple 1
        self.rules.append(
            Rule(['w', 'p', 'b', 'w'], [('i','we','you','they'), ('VVB','VVD','VVG','VVZ','VVN'),'.*',present_simple_kw],
                 ({'idx': 0}, {'idx':1 ,'tense': PRESENT, 'pronoun_idx': 0}, {'idx': 2,'until_word':present_simple_kw},{'idx':-1}))
        )  # Present Simple 2 PNP
        self.rules.append(
            Rule(['w', 'p', 'b', 'w'], [('he', 'she', 'it'), ('VVB','VVD','VVG','VVI','VVN'),'.*',present_simple_kw],
                 ({'idx': 0}, {'idx':1 ,'tense': PRESENT, 'pronoun_idx': 0}, {'idx': 2,'until_word':present_simple_kw},{'idx':-1}))
        )  # Present Simple 2 PNP
        self.rules.append(
            Rule(['p', 'p', 'b', 'w'], [('NN.','NP0'), ('VVB','VVD','VVG','VVI','VVN'),'.*',present_simple_kw],
                 ({'idx': 0}, {'idx':1 ,'tense': PRESENT, 'pronoun_idx': 0}, {'idx': 2,'until_word':present_simple_kw},{'idx':-1}))
        )  # Present Simple 2
        self.rules.append(
            Rule(['p','p', 'p', 'b', 'w'], [('NN.','NP0','PNP'), ('VBI'),('VVB','VVD','VVZ','VVN','VVI'),'.*',present_continuous_kw],
                 ({'idx': 0},{'idx':1}, {'idx':2 ,'tense': PARTICIPLE, 'pronoun_idx': 0}, {'idx': 3,'until_word':present_continuous_kw},{'idx':-1}))
        )  # Present Continuous

    def check(self, sentence: Sentence, verbose=False, max_iterations=10):
        for j in range(max_iterations):
            made_changes = False
            for rule in self.rules:
                i, win_len, possibility = rule.first_matched_window(sentence)
                if i != -1:
                    made_changes = True
                    sentence.problems.append([j, rule])
                    correct_window = rule.correct_window(sentence, i, win_len, possibility)
                    sentence.subsititue(
                        i, win_len, correct_window)
            if not (made_changes):
                break
            elif verbose:
                print(sentence.raw_sentence)

        return sentence
