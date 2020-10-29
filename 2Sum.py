# Time - O(nlogn)  Space - O(1)

def 2sum(nums,target):
    nums.sort()
    l, r = 0, len(nums) - 1
    while l < r:
        if nums[l] + nums[r] < target:
            l += 1
        elif nums[l] + nums[r] > target:
            r -= 1
        else:
            return [nums[l],nums[r]]
            
    return []    
    
    
    
# Time - O(n)  Space - O(n)

def 2sum(nums,target):
    lookup = set()            # dict is also perfectly fine.We dont use as it is not required.
    for x in nums:
        if target - x in lookup:
            return [target - x, x]
        lookup.add(x)
        
    return []
