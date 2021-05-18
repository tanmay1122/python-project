name=input("enter a name:- ")
total=""
i=0
while i<len(name):
    if name[i] not in total:
        total+=name[i]
        print(f"{name[i]}:{name.count(name[i])}")
        i+=1    