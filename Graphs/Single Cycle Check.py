""" 
Similar Qn But Not Same --> Circular Array Loop
"""

"""
Given a list of Intergers, which start from index = 0. 
Write a program to find if it consist only one cycle,
iee.... it should start from index 0 and end at index 0 without another cycle inside it

Input : [2, 3, 1, -4, -4, 2]
Output : True

"""

def SingleCycleCheck(nums):
    visitedElements, curidx = 0, 0
    while visitedElements < len(nums):
        
        if visitedElements > 1 and curidx == 0:
            return False
        visitedElements += 1
        curidx = getNextidx(curidx, nums)
        
    return curidx == 0

def getNextidx(idx, arr):
    jump = arr[idx]
    nextidx = (jump + idx) % len(arr)
    return nextidx if nextidx >= 0 else nextidx + len(arr)
