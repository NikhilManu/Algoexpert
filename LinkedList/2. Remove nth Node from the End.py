"""
-----------
Remove Nth Node From End of List [ Name of the Qn in LeetCode ]
-----------
"""
"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Input: head = [1,2,3,4,5], n = 2 
Output: [1,2,3,5]

Input is not an array. It is only a representation of the linked List
"""

# O(N) Time | O(1) Space
---------------
def NthnodeFromEnd(node,n):
    if not node:
        return node
    
    first = second = node
    for _ in range(n):
        second = second.next
        if not second:
            return node.next
        
    while second.next:
        first = first.next
        second = second.next
        
    first.next = first.next.next
    return node
   
 
 
  
