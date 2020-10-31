"""1.)  Given Array with distinct elements and a target value. Find 3 numbers such that their sum is equal to target value.

    Note: 1. Resultant array cannot contain duplicate triplets
          2. Given array nums does not contain duplicate elements.
"""

# Time - O(n^2)   Space - O(n)
def 3Sum(nums,target):
    nums.sort()
    for i in range(len(nums) - 2):
        l, r = i+1, len(nums) - 1
        while l < r:
            cur_sum = nums[i] + nums[r] + nums[l]
            if cur_sum == target:
                res.append([ nums[i], nums[l], nums[r] ])
                l += 1
                r -= 1
            elif cur_sum > target:
                r -= 1
            else:
                l += 1
                
    return res


"""1.)  Given an Array and a target value. Find 3 numbers such that their sum is equal to target value.

    Note: 1. Resultant array cannot contain duplicate triplets
          2. Given array nums can contain duplicate Elements
"""

# Time  - O(n^2)   Space - O(n)
def 3Sum(nums,target):
    nums.sort()
    for i in range(len(nums) - 2):
        
        if i > 0 and nums[i] == nums[i-1]:      #this case is important
            continue                            
            
        l, r = i+1, len(nums) - 1
        while l < r:
            cur_sum = nums[i] + nums[r] + nums[l]
            if cur_sum == target:
                res.append([ nums[i], nums[l], nums[r] ])
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                while l < r and nums[r] == nums[r-1]:
                    r -= 1
                l += 1
                r -= 1
            elif cur_sum > target:
                r -= 1
            else:
                l += 1
    return res
                
