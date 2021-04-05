example = [1897201031]

def descending_order(num):
    # convert integers to a sting
    num_str = str(num)
    # cast the string to a list
    num_list = list(num_str)
    # sort the list
    sort_nums = num_list.sort()
    # reverse the list
    result = sort_nums.revese()
    return result
    
print(descending_order(example))