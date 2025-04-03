# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(root,subRoot):
            if not root and not subRoot:
                return True
            if not root or not subRoot:
                return False
            if root.val != subRoot.val:
                return False
            return isSameTree(root.left,subRoot.left) and isSameTree(root.right,subRoot.right)

        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        res1 = False
        if root.val == subRoot.val:
            res1 = isSameTree(root,subRoot)
        if (res1):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right,subRoot)

        
        