def palindrome(nums):
    n=len(nums)
    left=0
    right=n-1
    while left<right:
        if nums[left]!=nums[right]:
            return False
        left+=1
        right-=1
    return True
    



nums = [1, 2, 3, 1]
print(palindrome(nums))