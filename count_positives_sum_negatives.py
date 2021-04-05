# Attempt 1
def count_positives_sum_negatives(arr):
    if not arr == None and len(arr) > 0: # considered an edge case code
        pos_count, neg_sum = [0, 0]
        neg_arr = []

        for x in arr:
            if x > 0:
                pos_count += 1
            elif x <= 0:
                neg_arr.append(x)
                neg_sum = sum(neg_arr)
    else:
        return ([])

    return [pos_count, neg_sum]


# Attempt 2
def count_positives_sum_negatives(arr):
    if not arr: 
        return []
    pos = 0
    neg = 0
    for x in arr:
      if x > 0:
          pos += 1
      if x < 0:
          neg += x
    return [pos, neg]

  


print(count_positives_sum_negatives([1, 2, 3, 4, 5, -11, -12, -13, -14, -15]))
print(count_positives_sum_negatives([]),[])