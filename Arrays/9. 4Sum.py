"""
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? 
Find all unique quadruplets in the array which gives the sum of target.

Notice that the solution set must not contain duplicate quadruplets.
Note : The array will not contain duplicate elements
"""
Time - avg-O(n^2)  | Space  - O(n^2)
def 4Sum(nums,target):
    res = []
    dic = {}
    for i in range(1,len(nums)-1):
        for j in range(i+1,len(nums)):
            cur = nums[i] + nums[j]
            diff = target - cur
            if diff in dic:
                for pairs in dic[diff]:
                    res.append(pairs + [nums[i],nums[j]])
                    
        for k in range(i):
            cur = nums[i] + nums[k]
            if cur not in dic:
                dic[cur] = [ [nums[i],nums[k] ]
            else:
                dic[cur].append( [nums[i],nums[k]] )
                            
    return res
               
            


"""
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? 
Find all unique quadruplets in the array which gives the sum of target.

Notice that the solution set must not contain duplicate quadruplets.
Note: The array can also contain duplicate elements

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

"""
#Solution 1 (Same as 3 SUm)
------------------------                            
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
                            
                            
# Solution 2 ---> 
----------------------------
# Time - O(n^2) for avg case  |   Space - O(n^2)



