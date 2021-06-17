def power(nu,*args):
    if args:
        return[i**nu for i in args]
    else:
        return "you dont pass any list or args"  

nu=[1,3,4,5,6]
print(power(2,*nu))