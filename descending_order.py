def descending_order(num):
    # Bust a move right here
    num2str = str(num)
    if(len(num2str) <= 1):
        return int(num2str)
    else:
        num_arr = list(num2str)
        num_arr.sort(reverse = True)
        # print(num_arr)
        whatever = int("".join(num_arr))
        return whatever

print( descending_order(123456789))