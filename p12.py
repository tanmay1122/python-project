def meet(n1,n2):
    if n1>n2:
        return n1
    return n2    
n=int(input("enter 1 number:->"))
m=int(input("enter 2 number:->"))
num=meet(n,m)
print(f"{num} is greater")