s = "swiss"
m={}
for char in s:
    if char not in m:
        m[char]=1
    else:
        m[char]+=1

for char in s:
    if m[char]==1:
        print(char)
        break
