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
            
            for i in range(len(q)):
                node = q.popleft()
                
                if node:
                    if i == 0:
                        res.append(node.val)
                    if node.right:
                        q.append(node.right)
                    if node.left:
                        q.append(node.left)
           
        return res 
# TC O(n)
#SC O(n)
      #  BFS, the queue can hold up to O(n/2) nodes in the worst case → space complexity = O(n).