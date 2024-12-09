# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        res = False
        def dfs(root):
            nonlocal res
            if res == True:
                return True
            if not root:
                return
            if root.val == subRoot.val:
                res = self.isSame(root, subRoot)
            dfs(root.left)
            dfs(root.right)
            return res
        return dfs(root)
    def isSame(self, root, subroot):
        if not root and not subroot:
            return True
        # chec if subroot  < = root
        # if not subroot:
        #     return True
        if root and subroot and root.val == subroot.val:
            l = self.isSame( root.left, subroot.left)
            r = self.isSame(root.right, subroot.right)
            return l and r
        else: 
            return False

        