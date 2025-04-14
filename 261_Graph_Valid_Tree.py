# 261. Graph Valid Tree
# Solved
# Medium
# Topics
# Companies
# Hint
# You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

# Return true if the edges of the given graph make up a valid tree, and false otherwise.

 

# Example 1:
# Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
# Output: true

# Example 2:
# Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
# Output: false
 

# Constraints:

# 1 <= n <= 2000
# 0 <= edges.length <= 5000
# edges[i].length == 2
# 0 <= ai, bi < n
# ai != bi
# There are no self-loops or repeated edges.


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #initialize
        map = {i:[] for i in range(n)}
        visit = set()
        
        # create map
        for s,d in edges:
            # as undirected
            map[s].append(d)
            map[d].append(s)
        
        def dfs(node, parent):
            visit.add(node)
            val = map[node]
            for neig in val:# iterate over edges for each node
                if neig == parent:
                    continue

                if neig in visit or not dfs(neig, node):
                        return False
            return True


        
        if not dfs(0, -1):
            return False
        if len(visit) == n:
            return True
        return False

        # TC O(E + V)
        # SC : adj lis O(E + V), viset set O(V), recursion stack O(V) = O(E + V)

           
        
