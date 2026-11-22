s = "Python123 Programming"
v=0
c=0
d=0
for char in s:
    if char.lower() in "abcdefghijklmnopqrstuvwxyz":
        if char in 'aeiou':
            v+=1
        else:
            c+=1
    elif char in '1234567890':
        d+=1
print("vowels: ",v)
print("Consonants: ",c)
print("Digits: ",d)
    