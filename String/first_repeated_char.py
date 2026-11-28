s = "programming"
m=""
for i in range(len(s)):
    if s[i] in m:
        print(s[i])
        break
    m+=s[i]

        