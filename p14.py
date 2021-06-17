# define a function which will take list contain number as input and return list contain square of every element

number=[1,2,3,4]      # normal method
for i in number:
    print(i*i)
    i=+1


# useing list function 
def square_list(l):         # function
    square=[]             # empty list to store a items
    for j in l:
        square.append(j**2)            # add the items after squareing 
    return square
numbr=list(range(1,11))
print(square_list(numbr))        