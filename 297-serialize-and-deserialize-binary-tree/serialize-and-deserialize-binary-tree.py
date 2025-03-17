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
        if not root:
            res.append("N")
        q = deque()
        
        q.append(root)
        while q:
            n = len(q)
            for i in range(n):
                node = q.popleft()
                if node:
                    res.append(str(node.val))
                    q.append(node.left)
                    q.append(node.right)
                else:
                    res.append("N")
        return ",".join(res)
         # TC O(N)
         # SC : stack , res => O(h)
         # WORST CASE O(N)
         # best case O(logN)
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        value = data.split(",")
        if value[0] == "N":
            return None
        root = TreeNode(int(value[0]))
        q = deque([root])
        index  = 1
        while q :
            # n = len(q)
            # for i in range(n):
                node = q.popleft()
                if value[index] != "N":
                    node.left =  TreeNode(int(value[index]))
                    q.append(node.left)
                index += 1
                if value[index] != "N":
                    node.right =  TreeNode(int(value[index]))
                    q.append(node.right)
                index += 1
        return root






        val = data.split(",")
        if val[0] == "N":
            return None
        root = TreeNode(int(val[0]))
        q = deque([root])
        ind = 1
        while q:
            node = q.popleft()
            if (val[ind]!= "N"):
                node.left = TreeNode(int(val[ind]))
                q.append(node.left)
            ind +=1
            if (val[ind]!= "N"):
                node.right = TreeNode(int(val[ind]))
                q.append(node.right)
            ind +=1
        return root
            
# Time complexity: 

# O(n)
# Space complexity: 

# O(n)     

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))