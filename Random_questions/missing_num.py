def missing_number(nums):
    n=len(nums)
    expected=n*(n+1)//2
    actual=0
    for num in nums:
        actual+=num
    return expected-actual


nums = [1,0,3]
print(missing_number(nums))
