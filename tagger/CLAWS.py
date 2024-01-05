from CLAWSTag import Tagger
from nltk import word_tokenize
# https://pypi.org/project/CLAWSTag/

def claws_tag(sentence):
    tagger = Tagger.Postag('c5', 'horiz').start()
    return tagger.start(word_tokenize(sentence))