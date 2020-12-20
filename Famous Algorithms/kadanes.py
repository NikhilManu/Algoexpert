"""
Maximum Subrray[leetCode]
"""
"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""

# Solution --
# Time O(N)  | Space O(1)
-----------------
def KadanesAlgorith(nums):
    localmax, globalmax = float('-inf'), float('-inf')
    for num in nums:
        localmax = max(num, localmax + num)
        globalmax = max(localmax, globalmax)
        
    return globalmax
  
