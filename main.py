from language.sentence import Sentence
from grammar.rule import Rule
from grammar.checker import Checker
def main():
    rule = Rule(['p', 'p'], ['DT0', 'NN0'],({'const':'the'},{'idx':1}))
    checker = Checker([rule])
    checked = checker.check(Sentence('i am a cat a cat'))
    # print(checked.raw_sentence)

if __name__ == '__main__':
    main()
