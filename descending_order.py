def descending_order(num):
    # Bust a move right here
    num_str = str(num)
    num_list = [char for char in num_str]
    num_list.sort(reverse=True)
    joined = "".join(num_list)
    print(num_list)
    print(joined)
    pass

print(descending_order(123456789))