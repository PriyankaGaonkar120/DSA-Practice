def reverse_array(nums):
    n=len(nums)
    for i in range(0,len(nums)):
        j=len(nums)-1,-1,-1
        nums[i],nums[j]=nums[j],nums[i]
    return nums
nums = [1, 2, 3, 4, 5]
print(reverse_array(nums))