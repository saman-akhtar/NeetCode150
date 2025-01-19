# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def dfs( root):
            if not root:
                return 0,0
            
            maxLdia,left = dfs(root.left)
            maxRdia, right = dfs(root.right)
            height = max(left, right) + 1
            cur_dia = left + right
            dia = max(cur_dia, maxRdia, maxLdia)
            return dia, height
        dia, height = dfs(root)
        return dia


       