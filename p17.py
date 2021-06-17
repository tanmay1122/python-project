# filter odd even
def filter(l):
    odd_l=[]
    even_l=[]
    for i in l:
        if i%2==0:
            even_l.append(i)
        else:
            odd_l.append(i) 
    nuum=[odd_l,even_l]
    return nuum
numbr=list(range(1,11))
print(filter(numbr))                      
