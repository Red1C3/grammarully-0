from grammar.checker import Checker
from language.sentence import Sentence

_test_pairs = [
    ('the only on i can think of', 'the only one i can think of'),
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
    if checked.raw_sentence == correct:
        return True
    else:
        return (checked.raw_sentence, correct)
