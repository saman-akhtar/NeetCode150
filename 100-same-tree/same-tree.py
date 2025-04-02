# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # more readabel format
        # more of false cases , so just focus on true
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        else:
            return False


        # APPROACH 2 WORKS: not optimized
        if not p and not q:
            return True
        if not p or not q:
            return False
        res = self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        
        
        if not res or p.val != q.val:
            return False
        return True
# TC O(n)
# SC O(h), where h=O(logn), for balancedd tree
# O(N) for degnerated tree        