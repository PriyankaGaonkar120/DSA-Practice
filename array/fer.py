def frequency(s):
    m={}
    for char in s:
        if char not in m:
            m[char]=1
        else:
            m[char]+=1
    for char in s:
        print(char,":",m[char])
s="programming"
frequency(s)