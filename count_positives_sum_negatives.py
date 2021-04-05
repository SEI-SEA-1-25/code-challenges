def count_positives_sum_negatives(arr):
    if(len(arr) ==0):
        return([])
    pos_count = 0
    neg_sum = 0
    for el in arr:
        if(el<0):
            neg_sum += el
        elif(el>0):
            pos_count += 1
    return([pos_count,neg_sum])