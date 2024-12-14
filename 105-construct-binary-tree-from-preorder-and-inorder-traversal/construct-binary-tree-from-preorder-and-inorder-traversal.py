# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#clarifying question 
# Does the input contain unique values?

# If the values in preorder and inorder are not unique, the inorder.index() operation could result in ambiguity about subtree boundaries. For the algorithm to work, values must be unique.

# If not unique, modifications like passing index maps of values to positions in inorder could solve it. But as is, assume values are unique.

# Are preorder and inorder valid?

# The function assumes preorder and inorder correspond to a valid binary tree. If this constraint isn't met, the tree construction won't be meaningful.

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:     
        if not preorder or not inorder:
            return None
            
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1: ])
        return root

# Time complexity: O(n ^2)
# Space complexity: O(n ^2)
        
        # 3 9 1 2 20 15 7 PRE
        # 1 9 2 3 15 20 7 IN

        