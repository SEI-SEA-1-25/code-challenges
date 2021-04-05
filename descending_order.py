def descending_order(num):
    # Bust a move right here
    num_str = str(num)
    num_list.sort(reverse=True)
    joined = "".join(num_list)
    print(num_list)
    print(joined)
    return joined
