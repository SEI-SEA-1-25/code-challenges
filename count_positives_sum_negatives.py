def count_positives_sum_negatives(arr):
    #your code here
    if (len(arr) < 1):
        return []
    new_array = [0,0]
    for i in range(len(arr)):
        if (arr[i] > 0):
            new_array[0] += 1
        else:
            new_array[1] += arr[i]
    return new_array
