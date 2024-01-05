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
        self.rules.append(Rule(['w', 'w', 'p'], ["more", ("a", "an"), 'AJ0'], ({
                          'idx': 1}, {'idx': 0}, {'idx': 2})))  # 4
        self.rules.append(Rule(['w', 'w', 'w'], ['think', 'you', ('a', 'an')], ({
                          'idx': 0}, {'idx': 1}, {'const': 'are'})))  # 5
        self.rules.append(Rule(['w', 'w'], [('some', 'certain'), 'extend'], ({
                          'idx': 0}, {'const': 'extent'})))  # 6
        self.rules.append(
            Rule(['w', 'w'], ['is', 'were'], ({'idx': 0}, {'const': 'where'})))  # 7
        self.rules.append(
            Rule(['p', 'w'], ['CRD', 'ore'], ({'idx': 0}, {'const': 'or'})))  # 8
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

    def check(self, sentence: Sentence, verbose=False, max_iterations=10):
        for _ in range(max_iterations):
            made_changes = False
            for rule in self.rules:
                i = rule.first_matched_window(sentence)
                if i != -1:
                    made_changes = True
                    correct_window = rule.correct_window(sentence, i)
                    sentence.subsititue(
                        i, rule.con_len, correct_window)
            if not (made_changes):
                break
            elif verbose:
                print(sentence.raw_sentence)

        return sentence
