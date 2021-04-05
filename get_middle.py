def get_middle(s):
    #your code here

    if len(s) %2 == 1:
        middle_index = len(s)// 2
        return s[middle_index]
    else:
        index1= len(s)// 2 - 1
        index2 = len(s)// 2 
        return s[index1] + s[index2]

s = 'book'

print(get_middle(s))