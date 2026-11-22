# Reverse a string without using [::-1].
s="hello"
r=""
for i in range(len(s)-1,-1,-1):
    r=r+s[i] 
print(r)