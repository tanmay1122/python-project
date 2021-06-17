def pname(name):                # 1 method
    reversed=name[::-1]
    if name==reversed:
        return True
    else:
        return False    
nn=input("enter a name:->")
eql=pname(nn)
print(eql)        

def pname1(name1):                # 1 method
    reversed1=name1[::-1]
    if name1==reversed1:
        return True
    else:
        return False    
nn1=input("enter a name:->")
print(pname(nn1))        


def pname2(name2):                # 2 method
    reversed2=name2[::-1]
    if name2==reversed2:
        return True
    return False    
nn2=input("enter a name:->")
print(pname(nn2))        


def pname3(name3):                # 3 method
    if name3==name3[::-1]:
        return True
    return False    
nn3=input("enter a name:->")
print(pname(nn3))        
