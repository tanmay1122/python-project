name=input("enter your name:->")     
def add(n,m):
   return n+m
def sub(n,m):
    return n-m
def multiply(n,m):
    return n*m
def divide(n,m):
   return n/m
print("welecome to my calculator")
while True:
    menu=input("a:add , s:subtraction , m:multiply , d:divide ::--->>>  ")
    if menu in('a','s','m','d'):
        n1=float(input("enter a first number:->"))
        n2=float(input("enter a second number:->"))

        if menu=='a':
            print(n1,'+',n2,'=',add(n1,n2))
            break
        if menu=='s':
            print(n1,'-',n2,'=',sub(n1,n2))
            break
        if menu=='m':
            print(n1,'*',n2,'=',multiply(n1,n2))
            break
        if menu=='d':      
            print(n1,'/',n2,'=',divide(n1,n2))      
            break
    else:
        print("any error is present")  
        break
print("thankyou",name)            