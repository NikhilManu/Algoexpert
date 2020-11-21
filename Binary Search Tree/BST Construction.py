"""
Construct a BST which have following functions,
Insertion
Searching
Deletion

"""

# Solution ---
# 
----------------
class BST:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None
        
    # O(LogN) Time and O(N) Time in  Worst | O(1) Space
    def insert(self, value):
        cur = self
        while True:
            if value < cur.val:
                if not cur.left:
                    cur.left = BST(value)
                    break
                else:
                    cur = cur.left
            elif value > cur.val:
                if not cur.right:
                    cur.right = BST(value)
                    break
                else:
                    cur = cur.right
                    
        return self
                
    # O(Log N) Time and O(N) in Worst Case | O(1) Space
    def search(self, value):
        cur = self
        while cur:
            if value < cur.val:
                cur = cur.left
            elif value > cur.val:
                cur = cur.right
            else:
                return True
        return False
    
    
    def delete(self, value, parent = None):
        cur = self
        while cur:
            if value < cur.val:
                parent = cur
                cur = cur.left
            elif value > cur.val:
                parent = cur
                cur = cur.right
            else:
                if cur.left and cur.right:
                    cur.val = cur.right.getMinValue()
                    cur.right.remove(cur.val, cur)   
                elif parent.left == cur:
                    parent.left = cur.left if cur.left else cur.right
                elif parent.right == cur:
                    parent.right = cur.left if cur.left else cur.right
                
                elif not parent:
                    if cur.left:
                        cur.val = cur.left.value
                        cur.left = cur.left.left
                        cur.right = cur.left.right
                    elif cur.right:
                        cur.val = cur.right.val
                        cur.left = cur.right.left
                        cur.right = cur.right.right
                    
                    else:
                        cur.val = None  
                        
                break
                    
    def getMinValue(self):
        cur = self
        while cur.left:
            cur = cur.left
        return cur.val
    
    
        
                
        
    
    


