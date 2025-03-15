# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        right = self.invertTree(root.right)
        left = self.invertTree(root.left)
        root.left ,root.right = right,left
        return root











        # if not root:
        #     return None
        # left = root.left
        # right = root.right
        
        # root.left , root.right = root.right ,root.left

        # self.invertTree(root.left)

        # self.invertTree(root.right)
        # return root
# TC O(N)    
# SC O(N) (recursion stack)
        
        