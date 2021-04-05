def count_positives_sum_negatives(arr):
    # Start with an empty array
    nums_array = []

    #Loop through the array, get all positive numbers, append them to nums_array, and display the length
    for num in arr:
        if num > 0:
            pos_num = nums_array.append(num)
            positives = len(pos_num)
            return positives
        elif num < 0:
            neg_num += nums_array.append(num)
            return nums_array
        elif num == False:
            num = []
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]

count_positives_sum_negatives(num)