"""
---------------
Rotate List [ Name of this Qn in Leetcode ]
--------------
"""
"""
Given a head of linked list and integer k, Rotate the linkedlist by k to the right if k is +ve.
Rotate to the left by k places if k is -ve.
"""

# Solution 1 ---> Corrected some mistakes in AlgoExpert Solution
# O(N) Time | O(1) Space
-------------------
def ShiftLinkedlist(head,k):
    if not head or k == 0:
        return head
    
    tailnode = head
    n = 1
    while tailnode.next:
        tailnode = tailnode.next
        n += 1
        
    offset = abs(k) % n
    if offset == 0: 
        return head
    pos = n - offset if offset > 0 else offset
    
    newtail = head
    for i in range(pos-1):
        newtail = newtail.next
    
    newhead = newtail.next
    newtail.next = None
    tailnode.next = head    
    
    return head


# Solution 2 ---> My Solution
# O(N) Time | O(1) Space
-------------------
def ShiftLinkedlist(head,k):
    node = head
    n = 1
    while node.next:
        node = node.next 
        n += 1
    node.next = head    # made a cycle
    
    offset = abs(k) % n
    pos = n - offset if k>=0 else offset
    node = head
    for _ in range(pos-1):
        node = node.next
    
    head = node.next
    node.next = None
    
    return head
        
    
    
    
  
