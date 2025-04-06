# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def dfs(root):
            nonlocal res
            if not root:
                res.append("N")
                return 
            res.append(str(root.val))
            dfs(root.left)
            
            dfs(root.right)
            return
        dfs(root)
        ans = ",".join(res)
        print("ANS",ans)
        return ans
        # n 2 n 1 3 4 5 
        # 1 2 n n 3 4 nul null 5 null nill
         # TC O(N)
         # SC : stack , res => O(h)
         # WORST CASE O(N)
         # best case O(logN)
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        res = data.split(",")
        self.i = 0
        # 1 2 n n 3 4 nul null 5 null nill
        def createTree():
            # base case
            if res[self.i] == "N":
                # also inc i so that we tell process nxt
                self.i += 1
                return None
            ch = res[self.i]
            node = TreeNode(int(ch))
            self.i += 1
            node.left = createTree()
            node.right = createTree()
            return node
        node = createTree()
        return node







            
# Time complexity: 

# O(n)
# Space complexity: 

# O(n)     

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))