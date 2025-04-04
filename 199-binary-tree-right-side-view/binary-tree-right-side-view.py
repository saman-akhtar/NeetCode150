# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        q = deque([root])
        while q:
            n = len(q)
            cur_res = []
            for i in range(n):
                node = q.popleft()
                if node:
                    cur_res.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if cur_res:
                res.append(cur_res[-1])
        return res

# TC ON
# SC ON

        #approach 1
    # def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    #     q = deque([root])
    #     res = []
    #     while q:
    #         qlen = len(q)
    #         for i in range(qlen):
    #             node = q.popleft()
    #             if node:
    #                 if node.right:
    #                     q.append(node.right)
    #                 if node.left:
    #                     q.append(node.left)
    #                 if i  == 0:
    #                     res.append(node.val)
    #     return res
# tc ON
# Sc O N
#n the worst case (for a balanced binary tree), the maximum number of nodes in the queue is the width of the tree, which occurs at the largest level of the tree.
