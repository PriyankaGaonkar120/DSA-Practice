# Remove duplicates from a list while preserving the original order, without using set().
arr = [1, 2, 3, 2, 4, 1, 5]
m=[]
for num in arr:
    if num not in m:
        m.append(num)
print(m)
