# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        order = defaultdict(list)
        q= deque()
        q.append((root,0,0))
        while q:
            n = len(q)
            for i in range(n):
                node, x,y = q.popleft()
                if node:
                    q.append((node.left, x+ 1, y -1))
                    q.append((node.right, x+ 1, y +1))
                    order[y].append((x, node.val))  # store row & value
                    # order[y].append(node.val)
        res = []
        for y in sorted(order):
            level = sorted(order[y])  # sorts by (x, val)
            res.append([val for x, val in level])
        return res


#         Step	Time	Space
# BFS Traversal	O(n)	O(n)
# Map Storage	O(n)	O(n)
# Sorting Keys (y)	O(k log k) ≤ O(n log n)	O(k)
# Sorting Values (x, val)	O(n log n)	O(n)
# Extracting Values	O(n)	O(n)
# ✅ Total
# \U0001f552 Time Complexity: O(n log n)

# \U0001f4be Space Complexity: O(n)