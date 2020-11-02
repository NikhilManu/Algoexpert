"""
-----------------------------------------------
Q  Shortest Unsorted Continuous Subarray [Name of Qn in LeetCode]
-----------------------------------------------

Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.

Return the shortest such subarray and output its length.

Input: nums = [2,6,4,8,10,9,15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.

Note: IN ALGOEXPERT WE RETURN THE INDICES, HERE WE RETURN THE LENGTH OF THE SUBARRAY

"""

# Time - O(n)  |  Space - O(1)
def Subarraysort(nums):
    if len(nums) <= 1:
        return 0
    
    small,big = float('inf'),float('-inf')
    for i in range(len(nums)):
        if isunsorted(i,nums):
            small = min(small,nums[i])
            big = max(big,nums[i])
            
    if small == float('inf'):    # or big == float('-inf') 
        return 0
    
    l,r = 0,len(nums) - 1
    while small >= nums[l]:
        l += 1
    while big <= nums[r]:
        r -= 1
        
    return r - l + 1

def isunsorted(i,nums):
    if i == 0:
        return nums[i] > nums[i+1]
    if i == len(nums) - 1:
        return nums[i] < nums[i-1]
    return nums[i] < nums[i-1] or nums[i] > nums[i+1]



# More types of solution are in leetcode.
        
