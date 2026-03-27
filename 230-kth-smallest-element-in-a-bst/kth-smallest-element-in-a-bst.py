# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res= []
        def dfs(root):
            nonlocal res
            if not root:
                return None
            dfs(root.left)
            if len(res)== k:
                return res
            res.append(root.val)
            if len(res)== k:
                return res
            dfs(root.right)
        dfs(root)
        return res[-1]
        