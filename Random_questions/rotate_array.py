def reverse(nums,left,right):
    while left<right:
        nums[left],nums[right]=nums[right],nums[left]
        left+=1
        right-=1
def rotate(nums, k):
    n=len(nums)
    if n==0:
        return
    k=k%n
    reverse(nums,0,n-1)
    reverse(nums,0,k-1)
    reverse(nums,k,n-1)



nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotate(nums,k)
print(nums)