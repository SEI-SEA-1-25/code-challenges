def get_middle(s):
    #your code here
if(len(s) % 2 ) == 1:
    index = (len(s) - 1) / 2
    return s[index]
else:
    start_index = int(len(s) / 2) - 1
    end_index = int(start_index + 1)
    return s[start_index : end_index + 1]

print(get_middle('Testing'))