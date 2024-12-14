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
        if not root:
            return "N"
        arr =[]
        q = deque([root])
        while q:
            qlen = len(q)
            for i in range(qlen):
                node = q.popleft()
                
                if node:
                    q.append(node.left)
                    q.append(node.right)
                    arr.append(str(node.val))
                else:
                    arr.append("N")
        return ",".join(arr)
                    
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
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