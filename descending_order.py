def descending_order(num):
    num_str = str(num)
    num_list = [char for char in num_str]
    num_list.sort(reverse=True)
    # num_list.reverse()
    # print(list(num_list))
    joined = ''.join(num_list)
    print(num_list)
    print(joined)
    return joined

print(descending_order(123456789))