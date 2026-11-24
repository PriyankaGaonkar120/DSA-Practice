s1 = "aabbc"
s2 = "abcab"
# Expected: Anagrams
if len(s1)!=len(s2):
    print("Not Anagrams")
s1d={}
s2d={}
for i in range(len(s1)):
    if s1[i] not in s1d:
        s1d[s1[i]]=1
    else:
        s1d[s1[i]]+=1
for i in range(len(s2)):
    if s2[i] not in s2d:
        s2d[s2[i]]=1
    else:
        s2d[s2[i]]+=1
if s1d==s2d:
    print("Anagrams")
else:
    print("Not Anagrams")

