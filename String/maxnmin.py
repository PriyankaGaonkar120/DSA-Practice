arr = [12, 5, 8, 21, 3, 17]
maxn=float ('-inf')
minn=float('inf')
for i in range(len(arr)):
    if arr[i]>maxn:
        maxn=arr[i]
    if arr[i]<minn:
        minn=arr[i]
print(maxn)
print(minn)