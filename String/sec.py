# Find the second-largest distinct number without using sort() or sorted().
arr = [5,5,5]
first=float('-inf')
sec=float('-inf')
for i in range(len(arr)):
    if arr[i]>first:
        sec=first
        first=arr[i]
    elif arr[i]>sec and arr[i]<first:
        sec=arr[i]

print(sec)