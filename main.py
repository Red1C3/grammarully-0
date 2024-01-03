from language.sentence import Sentence
from grammar.rule import Rule
def main():
    print(Rule.pattern_re_string([('a','an'),('NNP')]))

if __name__ == '__main__':
    main()
