
_ptb2bnc_map ={
    'CC' :['CJC'],
    'CD':['CRD'],
    'DT':['DT0','AT0'],
    'EX':['EX0'],
    'FW':['UNC'],
    'IN':['PRF','PRP'],
    'JJ':['AJ0'],
    'JJR':['AJC'],
    'JJS':['AJS'],
    'LS':['CRD'],
    'MD':['VM0'],
    'NN':['NN0','NN1'],
    'NNS':['NN2'],
    'NNP':['NP0'],
    'NNPS':['NP0'],
    'PDT':['DT0'],
    'POS':['POS'],
    'PRP':['PNP'],
    'PRP$':['PNP'],
    'RB':['AV0'],
    'RBR':['AV0','AJC'],
    'RBS':['AV0','AJS'],
    'RP':['AVP'],
    'TO':['TO0'],
    'UH':['UNC'],
    'VB':['VVI'],
    'VBD':['VVD'],
    'VBG':['VVG'],
    'VBN':['VVN'],
    'VBP':['VVI'],
    'VBZ':['VVZ'],
    'WDT':['DTQ'],
    'WP':['PNQ'],
    'WP$':['DTQ'],
    'WRB':['AVQ']
}

def PTB2BNC(penn_treebank_tagged_sentence):
    bnc_sent=[]
    for word_tag in penn_treebank_tagged_sentence:
        bnc_sent.append((word_tag[0],_ptb2bnc_map[word_tag[1]])) # Replace the Penn Treebank tag with BNC's
    return bnc_sent
