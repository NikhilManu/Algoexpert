""" 
-----------------
Merge Two Sorted List [ Name of this Qn in Leetcode ]
------------------
"""

"""
Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
"""

# Solution 1 ---> AlgoExpert Solution 1     # Solution 3 will be much Easier than this.
# O(N+M) Time | O(1) Space
-------------------
def MergeLinkedlist(l1,l2):
    p1,p2 = l1,l2
    prev = None
    while p1 and p2:
        if p1.val < p2.val:
            prev = p1
            p1 = p1.next
        else:
            if prev:
                prev.next = p2
            prev = p2
            p2 = p2.next
            prev.next = p1
            
    prev.next = p1 or p2
    return l1 if l1.val < l2.val else l2

# Solution 2 ---> AlgoExpert Solution 2 (Recursive Solution)
# O(N+M) Time | Space O(N + M)
---------------------
def MergeLinkedlist(l1,l2):
    helper(l1,l2,None)
    return l1 if l1.val < l2.val else l2

def helper(p1,p2,prev):
    if not p1:
        prev.next = p2
        return
    
    if not p2:
        return 
    
    if p1.val < p2.val:
        helper(p1.next,p2,p1)
    else:
        if prev:
            prev.next = p2
        newp2 = p2.next
        p2.next = p1
        helper(p1,newp2,p2)
        
 
# Solution 3 ---> My Solution 
# O(N+M) Time | O(1) Space
----------------------
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        
def mergeLinkedlist(l1,l2):
    if not l1:
        return l2
    if not l2:
        return l1
    
    dummy = Node('#')  # This is a Dummy Node
    cur = dummy
    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1   # if you dont create dummy and initialise cur as None. There will be a Error in this line
            l1 = l1.next
        else:
            cur.next = l2    # if you dont create dummy and initialise cur as None. There will be a Error in this line
            l2 = l2.next
        cur = cur.next
    cur.next = l1 or l2
    return dummy.next       # Return dummy.next, Not dummy
    

# Solution 3 ---> My Solution (Recursive) 
# O(N+M) Time | O(N+M) Space
----------------------
def MergeLinkedlist(l1,l2):
    if not l1 or not l2:
        return l1 or l2
    if l1.val < l2.val:
        l1.next = MergeLinkedlist(l1.next,l2)
        return l1
    else:
        l2.next = MergeLinkedlist(l1,l2.next)
        return l2
    
                                  
