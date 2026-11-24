def cnt(nums,target):
    count=0
    for i in range(len(nums)):
        if nums[i]==target:
            count+=1
    return count


nums = [1, 2, 3, 2, 2]
target = 2
print(cnt(nums,target))
