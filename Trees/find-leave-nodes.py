# """
# Definition of TreeNode:
# class TreeNode:
#     def __init__(self, val):
#         self.val = val
#         self.left, self.right = None, None
# """


# Description
# Given a binary tree, collect a tree's nodes as if you were doing this: Collect and remove all leaves, repeat until the tree is empty.

# LintCode - Online Judge Solution

# Candidate Written Test Screening, Team Competency Assessment, Programming Teaching Exercises, Online Exam Grading

# WeChat for information


# Example
# Example1
# Input: {1,2,3,4,5}
# Output: [[4, 5, 3], [2], [1]].
# Explanation:

#     1
#    / \
#   2   3
#  / \     
# 4   5    
# Example2
# Input: {1,2,3,4}
# Output: [[4, 3], [2], [1]].
# Explanation:

#     1
#    / \
#   2   3
#  /
# 4 
class Solution:
    """
    @param: root: the root of binary tree
    @return: collect and remove all leaves
    """
    def findLeaves(self, root):
        # write your code here
        def dfs(root, leaves):
            if not root:
                return None
            if  not root.left and not root.right:  
                leaves.append(root.val)
                return None
            root.left = dfs(root.left,leaves)
            root.right = dfs(root.right,leaves)
            return root
        res = []
        while  root:
            cur_res = []
            root = dfs(root,cur_res)
            res.append(cur_res)
        return res


# TC = O(N^2)'
# Baalcence = $N + \{N}/{2} + \frac{N}/{4} + .... + 1 = N
#SKEWED= $N + (N-1) + (N-2) ..... = N^2

# SC O(N)
#it's because of the Peak Stack Depth, not the total number of iter
# in eahc while loop stack trace is removed
