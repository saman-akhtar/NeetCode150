from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Step 1: Create the adjacency list for the graph
        adj = {i: [] for i in range(n)}
        for u, v, cost in flights:
            adj[u].append((v, cost))
        
        # Step 2: Set up DFS with memoization
        # Memoization will store the result of the cheapest cost for each (node, stops)
        memo = {}

        def dfs(node, stops):
            # If we reach the destination, return the cost 0
            if node == dst:
                return 0
            # If we've exceeded k stops, return infinity to prune
            if stops > k:
                return float('inf')
            if (node, stops) in memo:
                return memo[(node, stops)]
            
            # Step 3: Explore all neighboring nodes and accumulate the cost
            min_cost = float('inf')
            for neighbor, cost in adj[node]:
                next_cost = dfs(neighbor, stops + 1)
                if next_cost != float('inf'):
                    min_cost = min(min_cost, cost + next_cost)
            
            # Memoize and return the minimum cost found
            memo[(node, stops)] = min_cost
            return min_cost
        
        # Step 4: Start DFS from the src node
        result = dfs(src, 0)
        
        # Step 5: If result is still infinity, it means no valid path was found
        return result if result != float('inf') else -1
