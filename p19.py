def number_list(l):
    count=0
    for i in l:
        if type(i)==list:      # check the type of item if it is list then count increase otherwise nothing happen
            count+=1
    return count
name=([1,2,3,[],[1,2],["world","map","india"],["a","b","c"]]) 
print(number_list(name))   