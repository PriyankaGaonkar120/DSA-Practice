s = "programming"
result=""
for i in range(len(s)):
    if s[i] not in result:
        result+=s[i]
print(result)