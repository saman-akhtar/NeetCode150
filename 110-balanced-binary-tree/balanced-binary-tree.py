# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True
        def calculate(root):
            nonlocal res
            if not root:
                return 0
            leftc = calculate(root.left)
            rightc = calculate(root.right)
            # Check height difference
            if abs(leftc - rightc) >= 2:
                res = False
            return 1 +  max(leftc, rightc)
        
        calculate(root)
        return res
#Time Complexity: 
# \U0001d442
# (
# \U0001d45b
# )
# O(n), where 
# \U0001d45b
# n is the number of nodes
#
#Space Complexity: 
# \U0001d442
# (
# ℎ
# )
# O(h), where 
# ℎ
# h is the height of the tree.
# \U0001d442
# (
# log
# ⁡
# \U0001d45b
# )
# O(logn) for a balanced tree.
# \U0001d442
# (
# \U0001d45b
# )
# O(n) for a degenerate tree.