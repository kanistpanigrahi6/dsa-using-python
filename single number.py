def single_number(nums):
    res=0
    for i in range(len(nums)):
        res=res^nums[i]
        
    return res
print(single_number([4,4,4,2,2,1,2]))