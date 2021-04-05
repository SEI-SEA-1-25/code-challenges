# Your task is to make a function that can take
# any non-negative integer as an argument and
# return it with its digits in descending order.
# Essentially, rearrange the digits to create the highest possible number.

def descending_order(num):
    # Bust a move right here
    def myFunc(e):
        return e[0]

    str_num = str(num)
    new_list = [i for i in str_num]
    new_list.sort(reverse=True, key=myFunc)
    new_list = int(''.join(new_list))
    return new_list
    # loop through
    # if element is higher, append it, then pop it
    # while loop until original arr is empty

print(descending_order(345))