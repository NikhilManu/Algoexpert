"""
-------------
Reverse Linked List [ Name of this Qn in LeetCode ]
-----------
"""

"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
"""

#Solution 1 --> AlgoExpert 
# O(N) Time | O(1) Space
----------
def ReverseLinkedlist(head):
    node,prev = head,None
    while node:
        tmp = node.next
        node.next = prev
        prev = node
        node = tmp
    return prev

#Solution 2 ---> Without temp variable
# O(N) Time | O(1) Space
---------------
def ReverseLinkedlist(head):
    node,prev = head,None
    while node:
        node.next,prev,node = prev,node,node.next   # node,node.next,prev = node.next,prev,node ---> This will give a wrong Solution
    return prev 
        
# Solution 3 ---> Recursive Solution
# O(N) Time | O(N) Space
-----------------
def ReverseLinkedList(head):
    return helper(head,None)

def helper(node,prev):
    if not node:
        return prev
    
    cur = node.next
    node.next = prev
    return helper(cur,node)
  

