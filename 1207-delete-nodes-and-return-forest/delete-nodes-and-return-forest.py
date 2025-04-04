# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        res = []
        def delete(root, is_root):
            if not root:
                return None
            root_deleted =  root.val in to_delete
            if is_root and not root_deleted:
                res.append(root)
            root.left = delete(root.left, root_deleted)
            root.right = delete(root.right, root_deleted)
            return None if root_deleted else root
            


        delete(root, True)
        return res
        