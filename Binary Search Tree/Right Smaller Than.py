"""
 Count of Smaller Numbers After Self [ Name of this Qn in Leetcode ] ---> Not Sure if this is the Qn in AlgoExpert
 
"""

"""
You are given an integer array nums and you have to return a new counts array. 
The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

 

Example 1:

Input: nums = [5,2,6,1]
Output: [2,1,1,0]

Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
"""

# Time O(N LogN) and O(N) Space 
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None 
        self.duplicate = 1
        self.lessVal = 0
    
    def insert(self, val):
        if val == self.val:
            self.duplicate += 1
            return self.lessVal 
        elif val < self.val:
            self.lessVal += 1
            if not self.left:
                self.left = Node(val)
                return 0
            else:
                return self.left.insert(val)
        else:
            if not self.right:
                self.right = Node(val)
                return self.lessVal + self.duplicate
            else:
                return self.lessVal + self.duplicate + self.right.insert(val)
            
    
def RightSmaller(nums):
    res = [0] * len(nums)
    root = Node(nums[-1])
    for i in reversed(range(len(nums)-1)):
        res[i] = root.insert(nums[i])
        
    return res


