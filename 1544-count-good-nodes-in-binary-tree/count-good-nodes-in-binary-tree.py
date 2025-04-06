# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # CLARIFY - can nodes valiue be negative
    def goodNodes(self, root: TreeNode) -> int:
        maxN = float('-inf')
        self.count = 0
        def dfs(root, maxN):
            if not root:
                return
            if (maxN <= root.val):
                self.count += 1
                maxN = root.val
            dfs(root.left, maxN)
            dfs(root.right, maxN)
            return
        dfs(root,maxN)
        return self.count

# TC O(N)
# SC O(H)


        