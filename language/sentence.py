from tagger.PTB import penn_treebank_tag
from tagger.BNC import PTB2BNC

class Sentence:
    def __init__(self,sentence:str):
        self.raw_sentence=sentence
        self.problems=[]
    def get_bnc_tagged(self):
        return PTB2BNC(penn_treebank_tag(self.raw_sentence))