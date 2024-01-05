from tagger.PTB import penn_treebank_tag
from tagger.BNC import PTB2BNC
from tagger.CLAWS import claws_tag
from nltk import word_tokenize

class Sentence:
    START_TOKEN = ('SENT_START', ['SENT_START'])
    END_TOKEN = ('SENT_END', ['SENT_END'])
    def __init__(self,sentence:str):
        self.raw_sentence = Sentence.START_TOKEN[0] + ' ' + sentence + ' ' + Sentence.END_TOKEN[0]
        self.problems=[]
    def get_bnc_tagged(self):
        bnc = PTB2BNC(penn_treebank_tag(self.raw_sentence))
        bnc.insert(0, Sentence.START_TOKEN)
        bnc.insert(len(bnc), Sentence.END_TOKEN)
        return bnc

    def subsititue(self, i, length, correction: list[str]):
        list_of_str = word_tokenize(self.raw_sentence)
        for _ in range(length):
            list_of_str.pop(i)
        list_of_str.insert(i, correction)
        self.raw_sentence = str.join(' ', list_of_str)
   
    #def get_claws_tag(self):
        #claws_tag(self)