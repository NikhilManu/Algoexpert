"""
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? 
Find all unique quadruplets in the array which gives the sum of target.

Notice that the solution set must not contain duplicate quadruplets.
Note: The array can also contain duplicate elements

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

"""
# Time - O(n^3)  |   Space -  O(1) if resultant array is not considered else O(n)
def 4Sum(nums,target):
    result = []
    n = len(nums)
    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        for j in range(i+1, n-2):
            if j > i+1 and nums[j] == nums[j-1]:
                continue
            
            l,r = j+1,n-1
            while l < r:
                cur_sum = nums[i] + nums[j] + nums[l] + nums[r]
                if cur_sum < target:
                    l += 1
                elif cur_sum > target:
                    r -= 1
                else:
                    result.append([ nums[i],nums[j],nums[l],nums[r] ])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
    return result

# Solution is almost same as 3 sum
