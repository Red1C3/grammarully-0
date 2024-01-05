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
    ('i new it was a cat', 'i knew it was a cat'),
    ('please not that we are cats now', 'please note that we are cats now'),
    ('i am nut sure if i am a cat', 'i am not sure if i am a cat'),
    ('i am nut certain if i am a cat', 'i am not certain if i am a cat'),
    ('he went about being a cat and so one', 'he went about being a cat and so on'),
    ('i will through away the cat', 'i will throw away the cat'),  # He regrets it
    ('please not that you are nut sure if you are living in a simulation',
     'please note that you are not sure if you are living in a simulation'),
    ('or way that a cat', 'or was that a cat'),
    # ('thanks for the responds','thanks for the response') FIXME fails due to ambiguous tagging
    ('the only thing i can think off is cats', 'the only thing i can think of is cats'),
    # ('please do not us the cat','please do not use the cat') FIXME fails due to PTB2BNC mapping, force tag negation to XX0 tag to fix
    # ('i use to use the cat','i used to use the cat') FIXME fails because PTB never tags lexical verbs as special lexical verbs
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
