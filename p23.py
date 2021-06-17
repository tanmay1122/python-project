def input_list(l):
    return[str(i) for i in l if type(i)==int or type(i)==float]
print(input_list([1,1,2,3.3,[2,2,3,2],["d","e","e"]]))    