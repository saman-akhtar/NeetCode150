# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        # approach 2
        self.count = 0
        self.result = None
        def inorder(root):
            if not root :
                return
            inorder(root.left)
            self.count += 1
            if self.count == k:
                self.result = root.val
            inorder(root.right)
        inorder(root)
        return self.result


        # approach 1
        # res = []
        # def findSmall(root):
        #     if not root:
        #         return
        #     findSmall(root.left)
        #     res.append(root.val)
        #     findSmall(root.right)
        # findSmall(root)
        # return res[k-1]
        # tC O(N)
        # SC O(N) + O(h) => storing all node + call stack





        #approach 2

        arr = []
        cur = root
        stack = []
        n = 0
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            n += 1
            if (n == k):
                return cur.val
            
            cur = cur.right
    # TC O(N)
    # SC O(n)
        



        # recursive approach
        # arr = []
        # def findSmall(root):
        #     if not root:
        #         return 
        #     findSmall(root.left)
        #     arr.append(root.val)
            
        #     findSmall(root.right)
        # findSmall(root)
        # return arr[k-1]
# TC O(N)
# SC O(N) 

