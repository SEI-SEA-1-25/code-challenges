# You are going to be given a word.
# Your job is to return the middle character of the word.
# If the word's length is odd, return the middle character.
# If the word's length is even, return the middle 2 characters.

def get_middle(s):
    #your code here
    # use len and range to discover length of word
    # if odd length, return index of(length of string - 1 / 2 (9, i4)(13, i6))
    # if even, return (len)
    if (len(s) % 2) == 1:
        return s[int((len(s) - 1) / 2)]
    else: 
        even = s[int((len(s) / 2) - 1)], s[int(len(s) / 2)]
        return ''.join(even)

    


print(get_middle('Testing'))