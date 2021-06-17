# define a function that take list of word as a argument and return list with reverse of every element in the list
def rr(l):
    rl=[]
    for i in l:
        rl.append(i[::-1])
    return rl
numbr=["word","tanmay","anuradha","gopal","shyam"]
print(rr(numbr))                