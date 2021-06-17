# define a function which will take list as a arugment and this function will return a reversed list
# simple method 
name=[1,2,3,4]
print(name[::-1])

def r_l(l):
    l.reverse()
    return l
number=[1,2,3,4,5]
print(r_l(number))   

# use append nd pop method 
def reverse_list(l1):
    reverse_l=[]
    for i in range(len(l1)):
        num=l1.pop()                # pop l1 list first  and store it in num
        reverse_l.append(num)       # then add in blank list that is {reverse_l} by append method
    return reverse_l
numbr=list(range(1,11))
print(reverse_list(numbr))        
