# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]
        def dfs(root):
            if not root:
                return 0

            cur_path = root.val
            left = dfs(root.left)
            leftMax= max(left,0)
            right = dfs(root.right)
            rightMax= max(right,0)
            # cur path vs global max
            # compute max path sume with split
            res[0]= max(res[0], leftMax + rightMax + cur_path)

            # return root.val + either of left or right.. cant split twice
            return cur_path + max(leftMax,rightMax)
        dfs(root)
        return res[0]
        

# TC O(N)
# SC O(N) , O(logN) best case
        