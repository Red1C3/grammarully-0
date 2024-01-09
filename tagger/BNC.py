from pattern.text.en import INFINITIVE, PAST, PRESENT, PROGRESSIVE
from pattern.text.en import conjugate, tenses
from itertools import chain
import sys
from nltk.corpus import wordnet as wn

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
    'NNP-LOC': ['NP0'],
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

_possive_determinators = [
    'my', 'your', 'his', 'her', 'its', 'their', 'our'
]


def PTB2BNC(penn_treebank_tagged_sentence):
    bnc_sent = []
    for word_tag in penn_treebank_tagged_sentence:
        mapped_tags = _ptb2bnc_map[word_tag[1]]
        tags, merge = enhance_treebank_tag(word_tag[0], word_tag[1])
        if len(tags) > 0:
            if merge:
                mapped_tags = list(set(chain(mapped_tags, tags)))
            else:
                mapped_tags = tags
        bnc_sent.append((word_tag[0], mapped_tags))
    return bnc_sent


def enhance_treebank_tag(word, tbt):
    tags = []
    if word in _possive_determinators:
        tags.append('DPS')
    if word == 'not':
        return ['XX0'], False
    if tbt == 'MD':
        return tags, True
    inf_form = conjugate(verb=word, tense=INFINITIVE)
    if 'VB' in tbt:
        if inf_form == 'be':
            tags.append('VB' + ('I' if len(tbt) !=
                        3 or str(tbt[2]) == 'P' else str(tbt[2])))
        elif inf_form == 'do':
            tags.append('VD' + ('I' if len(tbt) !=
                        3 or str(tbt[2]) == 'P' else str(tbt[2])))
        elif inf_form == 'have':
            tags.append('VH' + ('I' if len(tbt) !=
                        3 or str(tbt[2]) == 'P' else str(tbt[2])))
        # This has increased the complexity A LOT
        elif len(sys.argv) > 1 and (sys.argv[1] == 'editor' or sys.argv[1] == 'tk'):
            v_tenses = tenses(word)
            if len(v_tenses) > 0:
                tags = list(
                    set(chain(*tags, *map(tense_to_tag, [v_tenses[0]]))))
    elif len(sys.argv) > 1 and (sys.argv[1] == 'editor' or sys.argv[1] == 'tk'):
        for tmp in wn.synsets(word, pos=wn.VERB):
            if tmp.name().split('.')[0] == inf_form and tmp.pos() == 'v':
                v_tenses = tenses(word)
                if len(v_tenses) > 0:
                    tags = list(
                        set(chain(*tags, *map(tense_to_tag, [v_tenses[0]]))))
                    break
    return tags, True


def tense_to_tag(tense_tuple):
    if INFINITIVE in tense_tuple:
        return ['VVI']
    if PRESENT in tense_tuple:
        if PROGRESSIVE in tense_tuple:
            return ['VVG']
        if 3 in tense_tuple:
            return ['VVZ']
        return ['VVB', 'VVI']
    if PAST in tense_tuple:
        if PROGRESSIVE in tense_tuple:
            return ['VVN']
        return ['VVD']
