class Rule:
    #construct: an array of either w or p values, indicating words or POS options
    #pattern: an array of possible choices for each construct
    # example:
    # construct: [w,p,w]
    # pattern: [(and,no),(NN0,NN1),(meow,cat)]
    def __init__(self, incorrect_construct, incorrect_pattern,correct_pattern=None,hint=None):
        self.construct=incorrect_construct
        self.incorrect_pattern=incorrect_pattern
        self.correct_pattern=correct_pattern
        self.hint=hint

    @staticmethod
    def pattern_re_string(pattern):
        string=[]
        for group in pattern:
            if type(group) is tuple:
                joined_group=str.join("|",group)
                joined_group='('+joined_group+')'
            else:
                joined_group=group
            string.append(joined_group)
        return str.join(' ',string)