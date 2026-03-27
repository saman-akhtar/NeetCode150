# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.path = float("-inf")
        def dfs(root):
            if not root:
                return 0
            lft = max(0, dfs(root.left))
            right =max(0, dfs(root.right))
            self.path = max(self.path, root.val + lft + right)
            return (root.val + max(lft, right))
        dfs(root)
        return self.path


# update global path: left + node + right
# return to parent: node + max(left, right)
        # Visit each node once.

# TC O(n)

# Space

# Recursion stack.

# Balanced tree → O(log n)
# Worst case → O(n)