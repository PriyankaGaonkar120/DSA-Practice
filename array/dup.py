def dup(arr):
    m=[]
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]==arr[j] and arr[i] not in m:
                m.append(arr[i])
    return m
arr = [1, 2, 3, 2, 4, 5, 1]
print(dup(arr))