"""
-------------------------
Longest Consecutive Sequence [Name of this Qn in LeetCode]
-------------------------
Given an unsorted array of integers nums, return the range of longest consecutive elements sequence.
We have to return [a,b], where a is smallest element in the range and b is the largest element in the range

Input: nums = [100,4,200,1,3,2]
Output: [1,4]
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].

"""
# Solution
# Time - O(n)  |  Space - O(n)
def largestRange(nums):
    dic = {x:True for x in nums}
    length = 0 
    res = []
    
    for i in nums:
        if not dic[i]:
            continue
        dic[i] = False
        cur_length = 1
        min_range = i-1
        max_range = i+1
        while min_range in dic:
            dic[min_range] = False
            min_range -= 1
            cur_length += 1
        while max_range in dic:
            dic[max_range] = False
            max_range += 1
            cur_length += 1
            
        if cur_length > length:
            res = [min_range + 1,max_range - 1]
            length = cur_length
            
    return res
            
            
  
