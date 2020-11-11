"""
Similar Qn --> Sort List [ Qn available in LeetCode ]
"""
"""
Given a head of linkedlist and a value k. Rearrange in the manner such that nodes before k should only contain node with value
less than that of k and nodes after k should only contain values greater than k

input: 2 -> 3 -> 5 -> 1 -> 4 , k=3
Output : 2 -> 1 -> 3 -> 5 -> 4

Note: The order should be maintained.
"""
# Solution
# O(N) Time | O(1) Space 
-------------------------
def RearrangeLinkedlist(head, k):
    smallerhead = None 
    smallertail = None
    equalhead = None 
    equaltail = None
    greaterhead = None 
    greatertail = None
    
    node = head
    while node:
        if node.val < k:
            smallerhead, smallertail = BuildLinkedlist(smallerhead, smallertail, node)
        elif node.val > k:
            greaterhead, greatertail = BuildLinkedlist(greaterhead, greatertail, node)
        else:
            equalhead, equaltail = BuildLinkedlist(equalhead, equaltail, node)
        prev = node
        node = node.next
        prev.next = None

    newHead, newTail = connectLinkedlist(smallerhear, smallertail, equalhead, equaltail)
    finalhead, _ = connectLinkedlist(newHead, newTail, greaterhead, greatertail)
    return finalhead
    
def connectLinkedlist(headOne, tailOne, headTwo, tailTwo):
    newhead = headTwo if not headOne else headOne
    newtail = tailOne if not tailTwo else tailTwo
    
    if tailOne:
        tailOne.next = headTwo
    
    return newhead, newtail

def BuildLinkedlist(head, tail, node):
    newhead,newtail = head, node
    
    if not newhead:
        newhead = node
    if tail:
        tail.next = newtail
        
    return newhead, newtail

    
