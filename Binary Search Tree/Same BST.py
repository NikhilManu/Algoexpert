"""
Given Two Array,
Check if they form the same BST
"""

# Solution 1----
# Time O(N^2) | Space O(N^2)
----------------------------
def sameBST(array1, array2):
    if len(array1) != len(array2):
        return False
    
    if len(array1) == len(array2) == 0:
        return True
    
    if array1[0] != array2[0]:
        return False
    
    left1, left2 = getSmaller(array1), getSmaller(array2)
    right1, right2 = getBiggerorEqual(array1), getBiggerorEqual(array2)
    
    return sameBST(left1, left2) and sameBST(right1, right2)


def getSmaller(arr):
    smaller = []
    for i in range(1, len(arr)):
        if arr[i] < arr[0]:
            smaller.append(arr[i])
    return smaller

def getBiggerorEqual(arr):
    biggerorEqual = []
    for i in range(1, len(arr)):
        if arr[i] >= arr[0]:
            biggerorEqual.append(arr[i])
    return biggerorEqual


# Solution 2 --- Improving the Space
# Time O(N^2) | O(d) Space
----------------------------
def SameBST(array1, array2):
    aresameBST(array1, array2, 0, 0, float('-inf'), float('inf'))

def aresameBST(array1, array2, rootidx1, rootidx2, minVal, maxVal):
    if rootidx1 == -1 or rootidx2 == -1:
        return rootidx1 == rootidx2
    
    if array1[rootidx1] != array2[rootidx2]:
        return False
    
    leftrootidx1, leftrootidx2 = getidxSmaller(array1, rootidx1, ), getidxSmaller(array2, rootidx2, )
    rightrootidx1, rightrootidx2 = getidxBigger(array1, rootidx1, ), getidxBigger(array2, rootidx2, )
    
    pass

def getidxSmaller(arr, startidx, minVal):
    for i in range(startidx + 1, len(arr)):
        if arr[i] < arr[startidx] and arr[i] >= minVal:
            return i
    return -1

def getidxSmaller(arr, startidx, maxVal):
    for i in range(startidx + 1, len(arr)):
        if arr[i] >= arr[startidx] and arr[i] < maxVal:
            return i
    return -1
    
        
    
    
