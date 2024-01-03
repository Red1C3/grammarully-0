from nltk import pos_tag,word_tokenize

def penn_treebank_tag(sentence):
    return pos_tag(word_tokenize(sentence))