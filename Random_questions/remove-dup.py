def remove_duplicates(nums):
    if len(nums)==0:
        return 0
    pos=0
    for i in range(1,len(nums)):
        if nums[pos]!=nums[i]:
            pos+=1
            nums[pos]=nums[i]
    k=pos+1
    return (k,nums[:k])
         
    

nums = [1, 1, 2]
print(remove_duplicates(nums))