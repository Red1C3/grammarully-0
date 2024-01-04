from language.sentence import Sentence
from grammar.rule import Rule
def main():
    rule = Rule(['p', 'p'], ['DT0', 'NN0'],({'const':'the'},{'idx':1}))
    error_idx=rule.first_matched_window(Sentence('i am a cat i am a cats'))
    print(rule.correct_window(Sentence('i am a cat i am a cats'),error_idx).raw_sentence)

if __name__ == '__main__':
    main()
