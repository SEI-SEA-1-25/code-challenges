def count_positives_sum_negatives(arr):
    #your code here
    if not arr or not len(arr):
        return []
    output = [0, 0]
    for number in arr:
        if number < 0:
            output [0] += 1
        elif number > 0:
            output[1] += number
    return output

    