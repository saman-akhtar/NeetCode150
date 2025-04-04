# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return root
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q) 
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q) 
        else:
            return root
        
     
    
        # asuuming p & q alway exist
        # TC O(log N) O(logn)(for balanced BST)orO(n)(for skewed BST)
        #.           he worst-case space complexity is:
# O(logn)(for balanced BST)orO(n)(for skewed BST)

        # @ SC O(logn)(for balanced BST)orO(n)(for skewed BST)
#         The recursive stack uses O(h) space, where h is the height of the tree.

# For a balanced BST, h = O(log n).

# For a skewed BST, h = O(n).
        
        
        
        # IF no recurion then improvement on space complexity
        # O (1)
        
        
        cur = root
        while cur:
            if p.val < cur.val and q.val < cur.val:
                cur = cur.left
            elif p.val > cur.val and q.val > cur.val:
                cur = cur.right
            else:
                return cur
# TC O Log n
# Space complexity: 
# O(1)      