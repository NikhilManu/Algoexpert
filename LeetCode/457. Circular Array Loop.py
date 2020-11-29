"""
You are given a circular array nums of positive and negative integers. If a number k at an index is positive, then move forward k steps.
Conversely, if it's negative (-k), move backward k steps. Since the array is circular, you may assume that the last element's next element is the first element, 
and the first element's previous element is the last element.

Determine if there is a loop (or a cycle) in nums. A cycle must start and end at the same index and the cycle's length > 1. 
Furthermore, movements in a cycle must all follow a single direction. In other words, a cycle must not consist of both forward and backward movements.

Example 1:
Input: [2,-1,1,2,2]
Output: true
Explanation: There is a cycle, from index 0 -> 2 -> 3 -> 0. The cycle's length is 3.

Example 2:
Input: [-1,2]
Output: false
Explanation: The movement from index 1 -> 1 -> 1 ... is not a cycle, because the cycle's length is 1. By definition the cycle's length must be greater than 1.

Example 3:
Input: [-2,1,-1,-2,-2]
Output: false
Explanation: The movement from index 1 -> 2 -> 1 -> ... is not a cycle, because movement from index 1 -> 2 is a forward movement, 
             but movement from index 2 -> 1 is a backward movement. All movements in a cycle must follow a single direction.
             
"""

def CircularArrayLoop(nums):
    for startidx in range(len(nums)):
        
        curidx, numberofVisited = startidx, 0
        direction = 1 if nums[curidx] > 0 else -1
        
        while numberofVisited < len(nums) and goingSameDirection(direction, nums[curidx]):
            nextidx = getNextidx(curidx, nums)
            numberofVisited += 1
            
            if curidx == startidx:
                if numberofVisited == 1:     # if numberofVIsited = 1, that means cycle length is 1 and that is not valid According to Qn
                    break
                              
                if numberofVisited > 1:
                    return True
        
    return False

def getNextidx(idx, arr):
    jump = arr[idx]
    nextidx = (jump + idx) % len(arr)
    return nextidx if nextidx >= 0 else len(arr) + nextidx

def goingSameDirection(direction, currentDirection):
    return direction * currentDirection > 0
