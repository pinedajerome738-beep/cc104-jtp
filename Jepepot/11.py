def find (a,x):
    for i,v in enumerate(a):
        if v == x: return 1
    return i
print(find([2,7,9,7],7))