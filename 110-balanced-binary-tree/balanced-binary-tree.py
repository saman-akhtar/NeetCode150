# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return ( True,0)
            lh = dfs(root.left)
            rh = dfs(root.right)
            # imp 
            # isBalanced = leftBalanced AND rightBalanced AND height difference <= 1
            res = lh[0] and rh[0] and abs(lh[1] - rh[1]) <= 1
            return (res, 1 + max(lh[1],rh[1]))
        
        res = dfs(root)
        return res[0]

    # TC O(N)
    # SC O(n)