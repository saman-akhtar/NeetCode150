class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:



        # WRONG
        # ISSUE is
        # “first found” back edge is not necessarily the extra edge as defined by the input order. For the “Redundant Connection” problem you must detect the edge whose addition creates the cycle according to the order of input.
        # DFS cycle detection on a graph that already contains all edges does not “know” the insertion order.
        # adj = defaultdict(list)
        # for s,d in edges:
        #     adj[s].append(d)
        #     adj[d].append(s)
        # visit = set()
        # def dfs(node, parent):
        #     visit.add(node)
        #     for neigh in adj[node]:
        #         if neigh == parent:
        #             continue
        #         if neigh in visit:
        #             return [neigh, node]
        #         res = dfs(neigh, node)
        #         if len(res) > 0:
        #             return res
        #     return []

        # res = dfs(1,-1)
        # if len(res) == 0:
        #     print(" There have be to be extrax edge, wrong input")
        #     return None
        # return res


        # SO COorect solutuon is
        # for easch edge before adding ot to map check if path exist and if already exist add and edge between
        # u & v will cause redundat 
        # so u have to run dfs for each edge
        # TC will be is O(e * (n + e)).
        


        # FINAL SOLUN
        #  NOTE A TREE is 1 ) comnnected. 2) has no cycle
        # USE The Union-Find data structure—also called the Disjoint Set Union (DSU)

        # GRAPH THERY : In tree N node otree have N -1 dges

        # In this problem we have N edges


        # IN union when u connect, conne smaller to larger component
        # which causes flattenr of tree so for eg 1 ->2.   now 3 is child of 2 but make it child fo 1 
        # so that we dont ahve to traverse long to know parent and tree is flaten
        # Going up the tree to find parent ; ackerman constant equl O(1)

        # intianliz
        n = len(edges)
        # edge start from 1
        par = [i for i in range(n + 1)] # each node is parnet fo itself
        rank = [ 1 ] * (n + 1)

        def find(x):
            if par[x] != x:
                par[x]= find(par[x])
            return par[x]

        def union(n1, n2):
            par1 = find(n1)
            par2 = find(n2)
            if par1 == par2:
                return False
            if rank[par1] > rank[par2]:
                # join shorter set to part of bigger
                par[par2] = par1
                # update rank
                rank[par1] += rank[par2]

            else:
                par[par1] = par2
                rank[par2] += rank[par1]
            return True
        
        # go thourgh each edge
        for u, v in edges:
            if not union(u,v):
                return [u,v]
            







        # tC O(V + E) * ackerman constant
        # SC O(V + E)