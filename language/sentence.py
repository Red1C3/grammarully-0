from tagger.PTB import penn_treebank_tag
from tagger.BNC import PTB2BNC
from nltk import word_tokenize

class Sentence:
    def __init__(self,sentence:str):
        self.raw_sentence=sentence
        self.problems=[]
    def get_bnc_tagged(self):
        return PTB2BNC(penn_treebank_tag(self.raw_sentence))

    def subsititue(self, i, length, correction: list[str]):
        list_of_str = word_tokenize(self.raw_sentence)
        for _ in range(length):
            list_of_str.pop(i)
        list_of_str.insert(i, correction)
        return str.join(' ', list_of_str)
