def descending_order(num):
    str_num = str(num)
    if (len(str_num) <= 1):
        new_num = int(str_num)
        return new_num
    else:
        new_list = []
        for i in str_num:
            new_num = int(i)
            new_list.append(new_num)
        new_list.sort(reverse = True)
        s = [str(i) for i in new_list]
        res = int("".join(s))
        return(res)

print(descending_order(12))