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
        if not preorder and not inorder:
            return None
        root_val = preorder[0]
        root = TreeNode(root_val)
        inorder_indx = inorder.index(root_val)
        # note imp: inorder_indx is ssame used in preorder to determine end of left part
        root.left = self.buildTree(preorder[1:inorder_indx+1], inorder[:inorder_indx])
        root.right = self.buildTree(preorder[inorder_indx+1:], inorder[inorder_indx+1:])
        return root








        if not preorder or not inorder:
            return None
            
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1: ])
        return root

# Time complexity: O(n ^2)
# Recursion Tree:

# The tree has 
# \U0001d442
# (\U0001d45b)
# O(n) nodes (one recursive call per node).
# At each node, the cost of inorder.index() is 
# \U0001d442(\U0001d45b)
# O(n).
# Thus, the total time complexity is:
# O(n ^2)
# Space complexity: O(n ^2)
# 1 Recursive Stack Space:
# The recursion depth depends on the height of the binary tree.
# In the worst case (a skewed tree), the recursion depth will be O(n).
# 2 Subarrays in Recursive Calls:
# Subarrays in Recursive Calls:

# At each recursive call, you create new subarrays (preorder[1:mid+1], inorder[:mid], etc.).
# These subarrays are slices of the input arrays, which involve copying elements.
# The total space used by subarray slicing across all recursive calls is proportional to the sum of the lengths of all these slices:
# \U0001d45b
# +
# (
# \U0001d45b
# −
# 1
# )
# +
# (
# \U0001d45b
# −
# 2
# )
# +
# ⋯
# +
# 1
# =
# \U0001d45b
# (
# \U0001d45b
# +
# 1
# )
# 2
# =
# \U0001d442
# (
# \U0001d45b
# 2
# )
# n+(n−1)+(n−2)+⋯+1= 
# 2
# n(n+1)
# ​
#  =O(n 
# 2
#  )


        
        # 3 9 1 2 20 15 7 PRE
        # 1 9 2 3 15 20 7 IN

        