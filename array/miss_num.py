def miss_nu(arr):
    m=arr[0]
    for i in range(1,len(arr)):
        if arr[i]!=m+1:
            return m+1
        m=arr[i]
    return None

arr = [1, 2, 4, 5, 6]
print(miss_nu(arr))