from language.sentence import Sentence
from grammar.rule import Rule
def main():
    rule = Rule(['p', 'w', 'p'], ['VVI', 'a', 'NN0'])
    print(rule.matched_windows(Sentence('i am a cat i am a cat')))
    print(Sentence('i am a cat i am a cat').get_bnc_tagged())

if __name__ == '__main__':
    main()
