example = 1897201031

def descending_order(num):
    # convert integers to a sting
    num_str = str(num)
    # cast the string to a list
    num_list = list(num_str)
    # sort the list
    num_list.sort()
    # reverse the list (using slicing operator)
    reversed = num_list[::-1]
    return reversed
    
print(descending_order(example))