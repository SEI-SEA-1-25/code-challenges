def count_positives_sum_negatives(arr):
    #your code here
    if arr == []:
        return []
    neg_sum = 0
    pos_sum = 0
    for num in arr:
        if num > 0:
            pos_sum += 1
            # print(pos_sum)
        if num < 0:
            neg_sum += num
            # print(neg_sum)
    return [pos_sum, neg_sum]

print (count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))
print (count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]))
print (count_positives_sum_negatives([]))

