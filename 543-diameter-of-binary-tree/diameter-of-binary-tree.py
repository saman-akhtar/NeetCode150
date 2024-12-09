# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        # Approach 2 
        # optimized
        def dfs(root):
            if not root:
                return 0, 0

            maxlh, maxLdia = dfs(root.left)
            maxrh, maxRdia = dfs(root.right)

                # cur height
            height = 1 + max(maxlh, maxrh)
            # cur dia
            cur_dia = maxlh + maxrh
            dia = max(cur_dia, maxLdia,maxRdia )
            return height, dia
        height, dia = dfs(root)
        return dia






        
        
        # Approach1

        # callculat diamter for every node 
        # dia = max Left height + max right height
        # to calculate that use 1 more recursion func: which calculate max of left height , right height


        # if not root:
    #             return 0
    #     maxLeft = self.findMaxdia(root.left)
    #     maxright = self.findMaxdia(root.right)
    #     dia =  maxLeft + maxright
    #     cur_dia = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
    #     return max(dia,cur_dia )
        
    # def findMaxdia(self, root):
    #     if not root:
    #         return 0
    #     cur_dia = 1 + max(self.findMaxdia(root.left) , self.findMaxdia(root.right))
    #     return cur_dia        
            
    # tc O n ^2
    # sc O (N)
        
        