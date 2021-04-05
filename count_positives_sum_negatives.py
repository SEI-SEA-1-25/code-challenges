def count_positives_sum_negatives(arr):
    # Begin positive numbers at 0
    pos_num = 0
    # Begin negative numbers at 0
    neg_num = 0
    # Start with an empty array
    nums_array = []

    #Loop through the array, get all positive numbers, append them to nums_array, and display the length
    for num in arr:
        if num > 0:
            pos_num = len(nums_array.append(num))
            return pos_num
        elif num < 0:
            neg_num += nums_array.append(num)
            return nums_array
        elif num == False:
            num = []

    

            




#Given an array of integers.

#Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers.

#If the input array is empty or null, return an empty array.