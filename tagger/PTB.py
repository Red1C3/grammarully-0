from nltk import pos_tag,word_tokenize
from pattern.en import parse


def penn_treebank_tag(sentence, strip_start_end=True,patter_parser=True):
    if patter_parser:
        parser = parse(sentence,chunks=False).split(" ")
        for i in range(len(parser)):
            parser[i]=parser[i].split("/")
        if strip_start_end:
            return parser[1:len(parser)-1]
        return parser
    if strip_start_end:
        tokenized = word_tokenize(sentence)
        return pos_tag(tokenized[1:len(tokenized) - 1])
    return pos_tag(word_tokenize(sentence))