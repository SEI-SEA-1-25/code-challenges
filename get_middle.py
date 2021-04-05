def get_middle(s):

    # if odd
    if len(s) % 2 == 1:
        index = (len(s) - 1) / 2
        return s[index]

    #if even
    else:
        start_index = int((len(s) / 2) - 1)
        end_index = int(start_index + 1)
        return s[start_index : end_index + 1]

    return ""


print(get_middle('Testing'))