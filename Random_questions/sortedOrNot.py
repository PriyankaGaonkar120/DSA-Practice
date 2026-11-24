def sort(nums):
    if len(nums)<=1:
        return True
    for i in range(len(nums)-1):
        if nums[i]>nums[i+1]:
            return False
    return True

nums = [1, 3, 2, 5]
print(sort(nums))
