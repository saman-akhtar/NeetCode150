# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#clarifying question ? will it contain unique value ??

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:     
        if not preorder or not inorder:
            return None
            
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1: ])
        return root

#TC O(N)
# SC O(1)
        
        # 3 9 1 2 20 15 7 PRE
        # 1 9 2 3 15 20 7 IN

        