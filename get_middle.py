def get_middle(s):
    len_s = len(s)
    print(len_s)
    return_value = ""
    if(len(s))==0:
        return("")
    elif(len_s%2 ==0):

        index_m = len(s)//2
        index_low = index_m - 1
        index_high = index_m + 1
        return_value = s[index_low:index_high]
    elif(len(s)%2==1):
        return_value = s[len(s)//2]
    print(return_value)
    return(return_value)

get_middle("test")#,"es")
get_middle("testing")#,"t")
get_middle("middle")#,"dd")
get_middle("A")#,"A")#
get_middle("of")#,"of")