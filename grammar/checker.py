from grammar.rule import Rule
from language.sentence import Sentence


class Checker:
    def __init__(self, rules: list[Rule]):
        self.rules = rules

    def check(self, sentence: Sentence, max_corrects=10):
        for _ in range(max_corrects):
            for rule in self.rules:
                i = rule.first_matched_window(sentence)
                if i != -1:
                    correct_window = rule.correct_window(sentence, i)
                    print(sentence.subsititue(i, rule.con_len, correct_window.raw_sentence))
                    return
