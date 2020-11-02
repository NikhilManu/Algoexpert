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
    res = [1] * len(nums)
    local_mins = localmin(nums)
    for i in local_mins:
        res = expand(i,nums,res)
    return sum(res)

def localmin(arr):
    if len(arr) == 1:
        return [0]
    local_mins =[]
    for i in range(len(arr)):
        if i == 0 and arr[i] < arr[i+1]:
            local_mins.append(i)
        if i == len(arr) - 1 and arr[i] < arr[i-1]:
            local_mins.append(i)
        if i == 0 or i == len(arr) - 1:
            continue
        if arr[i-1] > arr[i] < arr[i+1]:
            local_mins.append(i)

    return local_mins

def expand(i,nums,res):
    l = i - 1
    while l >= 0 and nums[l] > nums[l+1]:
        res[l] = max(res[l],res[l+1] + 1)
        l -= 1
    r = i + 1
    while r < len(nums) and nums[r] > nums[r-1]:
        res[r] = res[r-1] + 1
        r += 1
        
    return res


# Solution 3 ---> Left - Right Pass.
# Time  - O(n)  |  Space -  O(n)
def MinRewards(nums):
    res = [1] * len(nums)
    for i in range(1,len(nums)):
        if nums[i] > nums[i-1]:
            res[i] = res[i-1] + 1

    for i in range(len(nums)-2,-1,-1):
        if nums[i] > nums[i+1]:
            res[i] = max(res[i],res[i+1]+1)

    return sum(res)


** """
--------------
LeetCode Qn. Candy
--------------
This Qn is same as Min Rewards but the only difference is:
   -- The given array nums may contain duplicate elements
   
Input: [1,2,3,5,4,3,2,1,4,3,2,1,3,2,1,1,2,3,4]
Output: 47    

""" **

# Solution 1 ---> Naive Solution
# Time - O(n^2)  |  Space - O(n)
def MinRewards(nums):
    res = [1] * len(nums)
    for i in range(1,len(nums)):
        j = i - 1
        if nums[i] > nums[j]:
            res[i] = res[j] + 1
        elif num[i] < nums[j]: 
            while j >= 0 and nums[j] > nums[j+1]:
                res[j] = max(res[j] , res[j+1] + 1)
                j -= 1
        else:
            continue
    return sum(res)
# This is Almost Same As the Naive Qn of MIn Rewards


# Solution 2 ---> Left - Right Pass.
# Time  - O(n)  |  Space -  O(n)
def MinRewards(nums):
    res = [1] * len(nums)
    for i in range(1,len(nums)):
        if nums[i] > nums[i-1]:
            res[i] = res[i-1] + 1

    for i in range(len(nums)-2,-1,-1):
        if nums[i] > nums[i+1]:
            res[i] = max(res[i],res[i+1]+1)

    return sum(res)
# This Solution is Same as that of Min Rewards


"""
Solution 2 of Min Rewards is not used as when duplicate values are encountered. The Solution becomes more Complex.
"""


    
    
                
    
  


