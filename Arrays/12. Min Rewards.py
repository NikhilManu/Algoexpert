"""
-------------
Candy  [Name of this Qn in LeetCode]
-------------
"""

"""
Given a list of scores of students distribute them rewards such that
- all students must receive at least 1 reward
- any student must receive more rewards than any adjacent student with lower score & vice versa

Note: Each Score is Unique.

Return the minimum number of rewards you must give to the students

EXAMPLE:
Input : [8,4,2,1,3,6,7,9,5] 
Output : 25

"""
# Solution 1 ---> Naive Solution
# Time - O(n^2)  |  Space - O(n)
def MinRewards(nums):
    res = [1] * len(nums)
    for i in range(1,len(nums)):
        j = i - 1
        if nums[i] > nums[j]:
            res[i] = res[j] + 1
        else:
            while j >= 0 and nums[j] > nums[j+1]:
                res[j] = max(res[j] , res[j+1] + 1)
                j -= 1
    return sum(res)


# Solution 2 ----> Peak - Valley or Local min - Local Max Solution
# Time - O(n)  | Space - O(n)
def MinRewards(nums):
    
                
    
  


