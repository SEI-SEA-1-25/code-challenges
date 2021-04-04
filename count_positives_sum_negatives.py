# Given an array of integers.

# Return an array, where the first element 
# is the count of positives numbers and 
# the second element is sum of negative numbers.

# If the input array is empty or null, 
# return an empty array.

# Example:
# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 
# 10, -11, -12, -13, -14, -15], 
# you should return [10, -65].

arr1 = [20, 27, -80, 1, -23, 4]
arr2 = []


def count_positives_sum_negatives(arr):
    #set result as empty array
    result_arr = []
    if arr == [] : print("Bad input.")
    if arr:
        result_arr.append(sum([1 for x in arr if x > 0]))
        result_arr.append(sum([x for x in arr if x < 0]))
    return result_arr

print(count_positives_sum_negatives(arr2))