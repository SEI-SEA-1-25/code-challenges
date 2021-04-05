def descending_order(num):
    num_list = list(map(int, str(num)))
    num_list = sorted(num_list, reverse = True)
    output =  ''.join(map(str, num_list))
    return int(output)


    # num_str = str(num)
    # num_list = [char for char in num_str]
    # num_list.sort(reverse = True)
    # joined = "".join(num_list)
    # return num_list
