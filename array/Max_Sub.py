def max_subarray(nums):
    best=nums[0]
    cur=nums[0]
    for i in range(1,len(nums)):
        x=nums[i]
        if cur<0:
            cur=x
        else:
            cur+=x
        if cur>best:
            best=cur
    return best
nums = [5, 4, -1, 7, 8]
mx=max_subarray(nums)
print(mx)