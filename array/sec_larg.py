def second_largest(nums):
    first=None
    sec= None
    for x in nums:
        if first is None or x>first:
            sec=first
            first=x
        elif x!=first and(sec is None or x>sec):
            sec=x
    if sec is None:
        return -1
    
    return sec

nums = [10, 5, 20, 8]
sec=second_largest(nums)
print(sec)

