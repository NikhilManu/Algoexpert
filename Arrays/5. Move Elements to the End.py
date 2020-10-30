"""
Move Element To End
You are given an array of integers and an integer.
Write a function that moves all instances of that integer in the array to the end of the array.
The function should perform this in place and does not need to maintain the order of the other integers.

Sample input: [2, 1, 2, 2, 2, 3, 4, 2], 2
Sample output: [1, 3, 4, 2, 2, 2, 2, 2]  or  [4, 3, 1, 2, 2, 2, 2, 2]
"""

# Time - O(n) |  Space - O(1)
def MovetoEnd(nums,target):
    i,j = 0,len(nums) - 1
    while i < j:
        while i < j and nums[j] != target:
            j -= 1
        if nums[i] == target:
            nums[i],nums[j] = nums[j],nums[i]
        i += 1
    return nums


#if it is told to maintain relative order of other elements in array. ---> Similar Question - Move Zeroes (LeetCode).
Sample input: [2, 1, 2, 2, 2, 3, 4, 2], 2
Sample output: [1, 3, 4, 2, 2, 2, 2, 2]  #Here the order 1,3,4 should be maintained

# Time - O(n) |  Space - O(1)
def MovetoEnd(nums,target):
    i = 0
    for j in range(len(nums)):
        if nums[j] != target:
            nums[i],nums[j] = nums[j],nums[i]
            i += 1
            
    return nums
            
  
