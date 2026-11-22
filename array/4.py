arr = [1, 2, 3, 4, 5, 6]
e=0
o=0
for i in arr:
    if i%2==0:
        e+=1
    else:
        o+=1
print("Even:",e)
print("Odd:",o)