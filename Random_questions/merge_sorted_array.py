def merge(a,b):
    if len(a)<1:
        return b
    if len(b)<1:
        return a
    c=[]
    i=j=0
    while i<len(a) and j<len(b):
        if a[i]<b[j]:
            c.append(a[i])
            i+=1
        else:
            c.append(b[j])
            j+=1
    while i<len(a):
        c.append(a[i])
        i+=1
    while j<len(b):
        c.append(b[j])
        j+=1
    return c



a = [1, 3, 5]
b = []
print(merge(a,b))