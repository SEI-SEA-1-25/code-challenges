def descending_order(num):
    string_num = str(num)
    list_num = [char for char in string_num]
    list_num.sort(reverse=True)

    join_list = "".join(list_num)
    return join_list
