def twoSum(nums, target):
    i=0
    j=1
    while(i<len(nums)):
        while(j<len(nums)):
            if nums[i]+nums[j]==target:
                output=[i,j]
                print(output)
                return
            else:
                i=i + 1
                j= j + 1
                
nums=list(map(int, input('nums = ').split()))
target=int(input('target = '))
twoSum(nums, target)

