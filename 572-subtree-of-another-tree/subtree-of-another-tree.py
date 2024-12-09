# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        res = self.isSame(root, subRoot)
        if( res):
            return res
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSame(self, root, subroot):
        if not root and not subroot:
            return True
        if root and subroot and root.val == subroot.val:
            l = self.isSame( root.left, subroot.left)
            r = self.isSame(root.right, subroot.right)
            return l and r
        return False

    # TC for each node, check subroot node
    # O (N * m)

    # SC : O(N + M)

        