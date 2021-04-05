def count_positives_sum_negatives(arr):
    result_array = []
    pos_sum = 0
    neg_sum = 0
    for i in arr:
        if i > 0:
            pos_sum += 1
        else:
            neg_sum += i
    result_array = [pos_sum, neg_sum]
    return result_array