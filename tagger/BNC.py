from pattern.text.en import INFINITIVE, PAST, PRESENT, PROGRESSIVE
from pattern.text.en import conjugate, tenses
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

_possive_determinators=[
    'my','your','his','her','its','their','our'
]

def PTB2BNC(penn_treebank_tagged_sentence):
    bnc_sent = []
    for word_tag in penn_treebank_tagged_sentence:
        mapped_tags = _ptb2bnc_map[word_tag[1]]
        tags, merge = enhance_treebank_tag(word_tag[0], word_tag[1])
        if len(tags) > 0:
            if merge:
                mapped_tags = list(chain(mapped_tags, tags))
            else:
                mapped_tags = tags
        bnc_sent.append((word_tag[0], mapped_tags))
    return bnc_sent


def enhance_treebank_tag(word, tbt):
    tags = []
    if word in _possive_determinators:
        tags.append('DPS')
    if word =='not':
        return ['XX0'], False
    if 'VB' in tbt:
        inf_form = conjugate(verb=word, tense=INFINITIVE)
        if inf_form == 'be':
            tags.append('VB' + (str(tbt[2]) if len(tbt) == 3 else 'B'))
        elif inf_form == 'do':
            tags.append('VD' + (str(tbt[2]) if len(tbt) == 3 else 'B'))
        elif inf_form == 'have':
            tags.append('VH' + (str(tbt[2]) if len(tbt) == 3 else 'B'))
        # This has increased the complexity A LOT
        # else:
        #     v_tenses=tenses(word,parse=False)
        #     if len(v_tenses)==1:
        #         return tense_to_tag(v_tenses[0]),False
        #     for v_t in v_tenses:
        #         tags=list(chain(tags,tense_to_tag(v_t)))
    return tags, True


def tense_to_tag(tense_tuple):
    t = tense_tuple[0]
    person = tense_tuple[1]
    aspect = tense_tuple[3]
    if t == INFINITIVE:
        return ['VVI']
    if t == PRESENT:
        if aspect == PROGRESSIVE:
            return ['VVG']
        if person == 3:
            return ['VVZ']
        return ['VVB', 'VVI']
    if t == PAST:
        if aspect == PROGRESSIVE:
            return ['VVN']
        return ['VVD']
