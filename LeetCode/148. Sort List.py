"""
Given the head of a linked list, return the list after sorting it in ascending order.
"""

# Solution ---> Merge Sort
# O(NLogN) Time | O(LogN) Space
-----------------------------
def SortList(head):
    return SplitandSort(head)

def SplitandSort(head):
    if not head or not head.next:
        return head
    
    rightHead = findMiddleNode(head)
    
    left = SplitandSort(head)
    right = SplitandSort(rightHead)
    
    return merge(left, right)
    
def merge(h1, h2):
    if not h1 or not h2:
        return h1 or h2
    
    dummy = Node('#')
    node = dummy
    
    while h1 and h2:
        if h1.val < h2.val:
            node.next = h1.val
            h1 = h1.next
        else:
            node.next = h2.val
            h2 = h2.next
            
        node = node.next
        
    node.next = h1 or h2
    
    return dummy.next

def findMiddleNode(head):
    fast,slow = head, head
    temp = None
    while fast and fast.next:
        temp = slow
        slow = slow.next
        fast = fast.next.next
    
    tmp.next = None
    return slow
    
  
