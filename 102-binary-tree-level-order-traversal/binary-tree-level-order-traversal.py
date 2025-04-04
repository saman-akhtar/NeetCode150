# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque([root])
        res = []
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
                res.append(cur_res)
        return res
       


                    
        
# TC  O (N)
# SC O (N)