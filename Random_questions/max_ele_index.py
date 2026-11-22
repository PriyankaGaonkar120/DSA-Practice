def find_max(nums):
    idx=0
    mx=float('-inf')
    for i in range(len(nums)):
        if nums[i]>mx:
            mx=nums[i]
            idx=i
    return (mx,idx)



nums = [3, 9, 2, 9, 5]
print(find_max(nums))