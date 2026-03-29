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

        arr = []
        if not root:
            return ""
        q = deque([root])
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    arr.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                else:
                    arr.append("null")
        print("Arr",arr)

        return ",".join(map(str, arr))
                


        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        i = 1# start from second element
        arr = data.split(",")
        root = TreeNode(int(arr[0]))
        q = deque([root])
        n = len(arr)
        while q:
            node = q.popleft()
            if i < n:
                if arr[i] != "null":
                    new_node= TreeNode(int(arr[i]))
                    node.left = new_node
                    q.append(node.left)
                i += 1
            if i < n:
                if arr[i] != "null":
                    new_node= TreeNode(int(arr[i]))
                    node.right = new_node
                    q.append(node.right)
                i += 1
        
        
        return root
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))