def count_positives_sum_negatives(arr):
    #your code here
    array =[]
    pNum = 0
    nNum = 0
    if arr == [] or arr == None:
    
        return array
    else:
        for x in arr:
            if x > 0:
                pNum += 1

        for y in arr:
            if y < 0:
                nNum += y
        

        return [pNum,nNum]


arr=[3,-7,11,5,-2]
print(count_positives_sum_negatives(arr))