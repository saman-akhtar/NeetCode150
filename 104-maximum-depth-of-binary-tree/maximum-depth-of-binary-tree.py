# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = 1 +  self.maxDepth(root.left)
        right = 1 +  self.maxDepth(root.right)
        return max(left,right)



# TC O(N)
# SC best case O(logN)
#    worst case O(N)







    

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

# tc : O(N)
# Sc: height -> balanced tree O(log n)
#.           -> degerated tree : sort of limnked list -> total no of node O(N)
        