def get_middle(s):

    # str_len = len(s)
    # if str_len % 2 == 0:
    #     return(s[(str_len / 2 - 1): (str_len / 2 + 1)])
    # elif str_len % 2 > 0:
    #     return(s[str_len / 2])
    # else:
    #     return s

    return s[(len(s)-1) // 2 : (len(s)+2) // 2]