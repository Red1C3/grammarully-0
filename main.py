from tagger.PTB import penn_treebank_tag
from tagger.BNC import PTB2BNC

def main():
    ptb=penn_treebank_tag('i am a cat')
    print(PTB2BNC(ptb))

if __name__ == '__main__':
    main()
