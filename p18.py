# common elen=ment finder function
# define a function which take 2 list as input and return a list
# which contain common element of both list

def comon_list(l,m):
    com_l=[]
    for i in l:
        if i in m:
            com_l.append(i)
    return com_l
print(comon_list([1,2,3,4,5],[1,2,4,6,7,8]))                

