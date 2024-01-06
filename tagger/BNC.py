from pattern.text.en import INFINITIVE
from pattern.en import conjugate

_ptb2bnc_map = {
    'CC': ['CJC'],
    'CD': ['CRD'],
    'DT': ['DT0', 'AT0'],
    'EX': ['EX0'],
    'FW': ['UNC'],
    'IN': ['PRF', 'PRP'],
    'JJ': ['AJ0'],
    'JJR': ['AJC'],
    'JJS': ['AJS'],
    'LS': ['CRD'],
    'MD': ['VM0'],
    'NN': ['NN0', 'NN1'],
    'NNS': ['NN2'],
    'NNP': ['NP0'],
    'NNPS': ['NP0'],
    'PDT': ['DT0'],
    'POS': ['POS'],
    'PRP': ['PNP'],
    'PRP$': ['PNP'],
    'RB': ['AV0'],
    'RBR': ['AV0', 'AJC'],
    'RBS': ['AV0', 'AJS'],
    'RP': ['AVP'],
    'TO': ['TO0'],
    'UH': ['UNC'],
    'VBB': ['VVI'],
    'VBD': ['VVD'],
    'VBG': ['VVG'],
    'VBN': ['VVN'],
    'VBP': ['VVI'],
    'VBZ': ['VVZ'],
    'WDT': ['DTQ'],
    'WP': ['PNQ'],
    'WP$': ['DTQ'],
    'WRB': ['AVQ']
}


def PTB2BNC(penn_treebank_tagged_sentence):
    bnc_sent = []
    for word_tag in penn_treebank_tagged_sentence:
        if 'VB' in word_tag[1]:
            if 'VB' == word_tag[1]:
                word_tag = (word_tag[0], 'VBB')
            inf_form = conjugate(verb=word_tag[0], tense=INFINITIVE)
            if inf_form == 'be':
                word_tag = (word_tag[0], 'VB'+str(word_tag[1][2]))
                # Replace the Penn Treebank tag with BNC's
                bnc_sent.append((word_tag[0], [word_tag[1]]))
                continue
            elif inf_form == 'do':
                word_tag = (word_tag[0], 'VD'+str(word_tag[1][2]))
                # Replace the Penn Treebank tag with BNC's
                bnc_sent.append((word_tag[0], [word_tag[1]]))
                continue
            elif inf_form == 'have':
                word_tag = (word_tag[0], 'VH'+str(word_tag[1][2]))
                # Replace the Penn Treebank tag with BNC's
                bnc_sent.append((word_tag[0], [word_tag[1]]))
                continue
        # Replace the Penn Treebank tag with BNC's
        bnc_sent.append((word_tag[0], _ptb2bnc_map[word_tag[1]]))
    return bnc_sent
