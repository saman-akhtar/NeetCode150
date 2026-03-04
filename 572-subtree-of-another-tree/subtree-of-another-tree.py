# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(root, subRoot):
            if not root and not subRoot:
                return True
            if not root or not subRoot:
                return False
            #if matc
            if root.val != subRoot.val:
                return False
            
            return isSame(root.left,subRoot.left) and isSame(root.right,subRoot.right)
        # not match
        if not root:
            return False
        if isSame(root,subRoot):
            return True
            # if root & subroot not same. May be root children can be be same 
            # so call isSUbtree func next
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)

        # TC O(N *M) - for every root search for ery subrooot
        # SC O(H)