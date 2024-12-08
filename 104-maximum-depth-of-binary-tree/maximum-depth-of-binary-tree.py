# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def findHeight(root, height):
            if not root:
                return 0

            # if (root.left):
            #     findHeight(root.left, height)
            # if (root.right):
            #     findHeight(root.right, height)
            height = 1 + max(findHeight(root.right, height), findHeight(root.left, height))
            return height
        return findHeight(root, 0)

        