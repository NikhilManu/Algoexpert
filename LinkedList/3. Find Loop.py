"""
-------------------
Linked List Cycle II [ Name of this Qn in LeetCode ]
------------------
"""
"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

"""

# 
------------
def FindLoop(node):
    fast = slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            fast = head
            while fast != slow:
                fast = fast.next
                slow = slow.next
                
            return slow
        
    return None
  
