s = "banana"
m={}
for i in range(len(s)):
    if s[i] not in m:
        m[s[i]]=1
    else:
        m[s[i]]+=1
print(m)