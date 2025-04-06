# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path = float('-inf')
        def dfs(root):
            nonlocal max_path
            if not root:
                return 0
            
            left_path = max(dfs(root.left),0)
            right_path = max(dfs(root.right),0)
            cur_path = root.val  + left_path + right_path
            max_path = max(max_path, cur_path )
            return root.val + max(left_path, right_path) # there can only be 1 split.. alreay sploting at parent so return eoth left path or righ pathd
        dfs(root)
        return max_path
        

# TC O(N)
# SC O(N) , O(logN) best case
        