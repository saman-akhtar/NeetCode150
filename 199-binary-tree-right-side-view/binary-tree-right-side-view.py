# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque([root])
        res = []
        while q:
            qlen = len(q)
            for i in range(qlen):
                node = q.popleft()
                if node:
                    if node.right:
                        q.append(node.right)
                    if node.left:
                        q.append(node.left)
                    if i  == 0:
                        res.append(node.val)
        return res
