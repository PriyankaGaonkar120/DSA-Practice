s = "I love Python"
res=" "
m=s.split()
for c in m:
    for i in range(len(c)-1,-1,-1):
        res+=c[i]
    res+=" "
print(res.strip())