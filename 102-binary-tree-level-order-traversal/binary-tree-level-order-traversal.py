# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([root])
        result = []
        while q:
            qlen = len(q)
           
            res = []
            for i in range(qlen):
                node = q.popleft()
                if node:
                    res.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if res:
                result.append(res)

        return result

#         Time complexity: 
# O
# (
# n
# )
# O(n)
# Space complexity: 
# O
# (
# n
# )
# O(n)