from collections import defaultdict, deque
from typing import List
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Build adjacency list
        graph = defaultdict(list)
        for s, d, price in flights:
            graph[s].append((d, price))
        
        # Priority queue (min-heap) to store (cost, current_node, stops_left)
        heap = [(0, src, k + 1)]
        
        # Visited dictionary to track minimum costs with remaining stops
        visited = {}

        while heap:
            cost, node, stops = heapq.heappop(heap)

            # If we reach the destination, return the cost
            if node == dst:
                return cost
            
            # If we have stops left, explore neighbors
            if stops > 0:
                for neighbor, price in graph[node]:
                    new_cost = cost + price

                    # Only add to the heap if this path has better cost or more stops left
                    if (neighbor, stops - 1) not in visited or visited[(neighbor, stops - 1)] > new_cost:
                        visited[(neighbor, stops - 1)] = new_cost
                        heapq.heappush(heap, (new_cost, neighbor, stops - 1))
        
        # If no valid path is found
        return -1
