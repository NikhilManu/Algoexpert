"""
Given a binary tree, flatten it to a Singly linked list in-place. ( ie...Make the left of every node None)

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6

The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
"""

# Iterative Solution
# O(N) Time | O(1) Space
----------------------------
def FlattenBinaryTree(root):
    cur = root
    while cur:
        if cur.left:
            prev = cur.left
            while prev.right:
                prev = prev.right   # Traverse To rightMost node of left Subtree ( From Eg. we reach Node (4) )
                
            prev.right = cur.right  # We make current Node's right Subtree, prev Node's right 
            cur.right = cur.left   # THen we make current Node's left Subtree , the current Node's right Subtree
            cur.left = None     # Removing the left 
            
        cur = cur.right
        
    return root
                
"""
Visualization ---->

Initial Tree:

						1
					   / \
					  2   5
					 / \   \
					3   4   6
                    

Then,

						 1
					   / 
					  2   
					 / \   
					3   4   
                          \
                            5
                              \
                                6
                                 
                                 
Then,

						1
						  \
							2   
						   /  \   
						  3    4   
						     	 \
								   5
									 \
									   6
                                       
Then,

						1
						  \
							2   
						   /     
						  3    
					        \
							  4   
							    \
								  5
								    \
									  6
Then:

						1
						  \
							2
							  \
							    3    
								   \
									 4   
									   \
										 5
										   \
											 6
