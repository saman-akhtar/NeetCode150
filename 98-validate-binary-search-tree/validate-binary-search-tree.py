# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root,low,high):
            if not root:
                return True
            if root.val <= low or root.val >= high:
                return False
            return (helper(root.left, low,root.val) and helper(root.right, root.val, high))


        return helper(root, float('-inf'), float('inf'))





    # WRONG AS it be less that root .. all left shoudl be less that root ..n ot immediate one
    
        # if not root :
        #     return True
        # if root.right and root.right.val <= root.val :
        #     return False
        # if root.left and root.left.val >= root.val:
        #     return False
        # return self.isValidBST(root.left) and self.isValidBST(root.right)

                                                                                                                                                                                                                                              



        # if not root:
        #     return True
        # if root.left:
        #     if root.left.val >= root.val:
        #         return False
        # if root.right:
        #     if root.right.val <= root.val:
        #         return False
        # return self.isValidBST( root.left) and  self.isValidBST( root.right)
    # Incorrect logic as all nOde on left shoulkd be < root
    # eg:     
#        5
#       / \
#      3   8
#     / \
#    2   6
#  6 < 5 , EDGE case


# CORRECT APPROACH
        def isValid(root, left,right):
            if not root:
                return True
            if not( left < root.val < right):
                return False
            return isValid(root.left,left, root.val) and isValid(root.right,root.val, right)
        return isValid(root, float('-inf'), float('inf'))








        def isValid( root, left, right):
            if not root:
                return True
            if not( left < root.val < right):
                return False
            # max val of left is root.val
            # ,min val of right is root.val
            return isValid( root.left, left, root.val) and isValid( root.right, root.val, right)
        return isValid(root, float('-inf'), float('inf'))


 # TC ON
 # SC O(N)       
        
        