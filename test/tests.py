from grammar.checker import Checker
from language.sentence import Sentence

_test_pairs = [
    ('the only on i can think of', 'the only one i can think of'),
    ('i can give you more a detailed cat', 'i can give you a more detailed cat'),
    ('some would think you a fortunate cat',
     'some would think you are fortunate cat'),
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
    ('he went about being a cat and so one',
     'he went about being a cat and so on'),
    ('i will through away the cat', 'i will throw away the cat'),  # He regrets it
    ('please not that you are nut sure if you are living in a simulation',
     'please note that you are not sure if you are living in a simulation'),
    ('or way that a cat', 'or was that a cat'),
    ('thanks for the responds', 'thanks for the response'),
    ('the only thing i can think off is cats',
     'the only thing i can think of is cats'),
    ('please do not us the cat','please do not use the cat'),
    # ('i use to use the cat','i used to use the cat'), #FIXME fails because PTB never tags lexical verbs as special lexical verbs
    ('i thing it is a good idea', 'i think it is a good idea'),
    ('he thing so', 'he thinks so'),
    ('we things about it', 'we think about it'),
    # ('were are you now','where are you now'), #FIXME fails because PTB does not have a special tag for "be" verb
    ('he has two cats not too dogs', 'he has two cats not two dogs'),
    ('we are not too far from home', 'we are not too far from home'),
    ('he has one cat not too', 'he has one cat not two'),
    # ('i think your confused about it', 'i think you are confused about it'),
    # ('he is less weirder then his cat', 'he is less weirder than his cat'),
    ('he is more cat then his cat', 'he is more cat than his cat'),
    ('the the cat is nice', 'the cat is nice'),
    ('what do you mean than', 'what do you mean then'),
    ('i am eager to trying out dying', 'i am eager to try out dying'),
    ('i a eager to trying out dying', 'i am eager to try out dying'),
    ('should we eat or', 'should we eat'),
    ('this is the most oldest cat here','this is the oldest cat here'), #FIXME the tagger is deciding it is an adj because it is after the most
    ('this is the more largest cat i have ever seen',
     'this is the largest cat i have ever seen'),
    ('i think is should be a good cat', 'i think it should be a good cat'),
    ('i did visited the cat', 'i did visit the cat'),
    ('i did went to the cat', 'i did go to the cat'),
    # ('he is go home', 'he is gone home'), #FIXME fails because the tagger assumes go adjactive
    ('his cat is as big like mine', 'his cat is as big as mine'),
    ('his cat is as large than mine', 'his cat is as large as mine'),
    ('his cat is as small then my cat', 'his cat is as small as my cat'),
    ('we can not run from the cat forever', 'we cannot run from the cat forever'),
    ('i am not larger that you', 'i am not larger than you'),
    ('the tagger will return more then one tag',
     'the tagger will return more than one tag'),  # true story
    ('the tagger will return less as five tags',
     'the tagger will return less than five tags'),
    ('this cat is larger then me', 'this cat is larger than me'),
    ('this cat is smaller as me', 'this cat is smaller than me'),
    ('your gone', 'you are gone'),
    ('its a good life we lead my brother', 'it is a good life we lead my brother'),
    ('its the choice my cat made', 'it is the choice my cat made'),
    ('its going to be a cute cat', 'it is going to be a cute cat'),
    ('no is not the right time', 'now is not the right time'),
    ('no you can not feed the cat', 'no you cannot feed the cat'),
    ('of cause all cats are cute', 'of course all cats are cute'),
    ('the study of cause and effect is fundamental to understanding cats',
     'the study of cause and effect is fundamental to understanding cats'),
    ('the principle of cause to effect is a cornerstone of understanding cats',
     'the principle of cause to effect is a cornerstone of understanding cats'),
    ('then he look after the cats', 'then he looks after the cats'),
    ('will he look after the cats','will he look after the cats'),
    ('should he pat the cats','should he pat the cats'),
    ('John will see the cats','John will see the cats'),
    ('I will feed the cats','I will feed the cats'),
    ('John might forgets to feed the cats','John might forget to feed the cats'), #FIXME the tagger is deciding "forgets" is an VVI
    # ('John will was a cat lover','John will be a cat lover'), #FIXME the tagger is deciding "was"" is an VVD
    # ('I will am a cat lover','I will be a cat lover'), #FIXME the tagger is deciding "am"" is an VVI
    # ('she will was a cat lover','she will be a cat lover'), #FIXME the tagger is deciding "was"" is an VVD
    ('she might looks for the cats','she might look for the cats'),  #FIXME the tagger is deciding "looks" is an VVI
    ('does someone please please can can a can',
     'can someone please please can a can'),
    ('we are a cats', 'we are the cats'),
    # ('the cats likes you','the cats like you'), #FIXME not working due to the tagger tagging likes VVI, works when heavy verbs conjugator is on
    ('Mike always went to feed cats', 'Mike always goes to feed cats'),
    ('He often go to feed cats', 'He often goes to feed cats'),
    ('i never go to kick cats', 'i never go to kick cats'),
    ('Jordan patted cats always', 'Jordan pats cats always'),
    # ('She look after cats every Sunday', 'She looks after cats every Sunday'),
    ('I seen cats daily', 'I see cats daily'),
]


def run_tests(max_iterations=10, verbose=False):
    c = Checker()
    for t in _test_pairs:
        res = _test(t[0], t[1], c, max_iterations)
        if res != True:
            print('TEST FAILED:')
            print(t[0]+' -> ' + t[1])
            print('CHECKER RESULT:')
            print(res[0])
            print('Used rules:')
            for rule in res[2]:
                print('index:', rule[0], '| Rule:', rule[1])
            print('='*20)
        elif verbose:
            print('TEST PASSED')
    print('FINISHED TESTING')


def _test(incorrect: str, correct: str, checker: Checker, max_iterations):
    incorrect_sent = Sentence(incorrect)
    checked = checker.check(incorrect_sent, False, max_iterations)
    if checked.raw_sentence == Sentence(correct).raw_sentence:
        return True
    else:
        return (checked.raw_sentence, correct, incorrect_sent.problems)
