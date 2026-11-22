s = "1122334455"
m={}
for d in s:
    if d not in m:
        m[d]=1
    else:
        m[d]= m[d] + 1
print(m)