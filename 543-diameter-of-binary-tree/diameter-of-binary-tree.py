# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            cur_dia = left + right
            self.res  = max(self.res, cur_dia)
            return  1 + max(left,right)
        dfs(root)
        return self.res 

      



       # TC O(N)
       # SC height of logn or O(n) if skewed