from nltk import pos_tag,word_tokenize


def penn_treebank_tag(sentence, strip_start_end=True):
    if strip_start_end:
        tokenized = word_tokenize(sentence)
        return pos_tag(tokenized[1:len(tokenized) - 1])
    return pos_tag(word_tokenize(sentence))