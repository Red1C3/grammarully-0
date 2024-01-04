from grammar.rule import Rule
from language.sentence import Sentence


class Checker:
    def __init__(self, *args):
        if len(args) != 0:
            self.rules = args[0]
        else:
            self.rules = []
        self.initRules()

    def initRules(self):
        self.rules.append(Rule(['w', 'w', 'p'], ["more",("a","an"), 'AJ0'],({'idx':1},{'idx':0},{'idx':2}))) #4

    def check(self, sentence: Sentence, max_corrects=10):
        for _ in range(max_corrects):
            made_changes = False
            for rule in self.rules:
                i = rule.first_matched_window(sentence)
                if i != -1:
                    made_changes = True
                    correct_window = rule.correct_window(sentence, i)
                    sentence = Sentence(sentence.subsititue(i, rule.con_len, correct_window.raw_sentence))
            if not(made_changes):
                break
            else:
                print(sentence.raw_sentence)

        return sentence
