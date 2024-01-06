from pattern.text.en import INFINITIVE
from pattern.text.en import conjugate
from itertools import chain

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
    'VB': ['VVI'],
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
        tags = enhance_treebank_tag(word_tag[0], word_tag[1])
        # Replace the Penn Treebank tag with BNC's
        bnc_sent.append((word_tag[0], list(chain(*[_ptb2bnc_map.get(x, [x]) for x in tags]))))
    return bnc_sent


def enhance_treebank_tag(word, tbt):
    tags = [tbt]
    if 'VB' in tbt:
        inf_form = conjugate(verb=word, tense=INFINITIVE)
        if inf_form == 'be':
            tags.append('VB' + (str(tags[0][2]) if len(tbt) == 3 else 'B'))
        elif inf_form == 'do':
            tags.append('VD' + (str(tags[0][2]) if len(tbt) == 3 else 'B'))
        elif inf_form == 'have':
            tags.append('VH' + (str(tags[0][2]) if len(tbt) == 3 else 'B'))
    return tags
