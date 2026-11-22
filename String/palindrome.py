s="madam"
r=""
for i in range(len(s)-1,-1,-1):
    r=r+s[i]
if s==r:
    print("Palindrome")
else:
    print("Not Palindrome")