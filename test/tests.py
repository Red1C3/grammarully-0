from grammar.checker import Checker
from language.sentence import Sentence

_test_pairs = [
    ('the only on i can think of', 'the only one i can think of'),
    ('i can give you more a detailed cat', 'i can give you a more detailed cat'),
    ('some would think you a fortunate cat', 'some would think you are fortunate cat'),
    ('yes it is to some extend', 'yes it is to some extent'),
    ('no it is not to a certain extend', 'no it is not to a certain extent'),
    ('this is were i found my cat', 'this is where i found my cat'),
    ('do you have one ore more cats', 'do you have one or more cats'),
    ('their are some cats here', 'there are some cats here'),
    ('i an a cat', 'i am a cat'),
    ('i a a cat', 'i am a cat'),
    ('i new it was a cat', 'i knew it was a cat')
]


def run_tests(max_iterations=10):
    c = Checker()
    for t in _test_pairs:
        res = _test(t[0], t[1], c, max_iterations)
        if res != True:
            print('TEST FAILED:')
            print(t[0]+' -> ' + t[1])
            print('CHECKER RESULT:')
            print(res[0])
            print('='*20)
    print('FINISHED TESTING')


def _test(incorrect: str, correct: str, checker: Checker, max_iterations):
    checked = checker.check(Sentence(incorrect), False, max_iterations)
    if checked.raw_sentence == Sentence(correct).raw_sentence:
        return True
    else:
        return (checked.raw_sentence, correct)
