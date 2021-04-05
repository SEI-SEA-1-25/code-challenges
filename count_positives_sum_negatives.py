def count_positives_sum_negatives(arr):
    #your code here

def count_positives_sum_negatives(arr):
    sum = 0
    count = 0
    new_arr = []
    for num in arr:    
        if num > 0:
#             print("I'm great😊", num)
            count += 1            
        elif num < 0:
            sum += num
    # if array = 0, return empty array
        else:
            arr = new_arr
    new_arr.append(count)
                
    new_arr.append(sum)
    
count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15])
