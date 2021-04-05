# Given an array of integers.

# Return an array, where the first element is the count of positives numbers
# and the second element is sum of negative numbers.

# If the input array is empty or null, return an empty array.


def count_positives_sum_negatives(arr):
    #your code here
    if (arr):
        pos = [i for i in arr if i > 0]
        neg = [i for i in arr if i < 0]
        final = [(len(pos_arr)), sum(neg_arr)]
    else:
        final = []
    return final
    # loop through array
    # if positive, add to pos_arr
    # if neg, add to neg_arr
    # then loop each again
    # first element is length of pos_arr
    # second element is sum of neg_arr

