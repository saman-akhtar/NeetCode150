class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # DIJIKSTRA: BFS algo
        # diff is uses min heap
        adj_list = defaultdict(list)
        for u,v,w in times:
            adj_list[u].append((v,w))
        visit = set()
        t = 0
        minHeap= [(0,k)] # path,node
        #BFS
        while minHeap:
            w1,node = heapq.heappop(minHeap)
            if node in visit :
                continue
            visit.add(node)
            t = max( w1,t)
            for node2 , w2 in adj_list[node]:
                if node2 not in visit:
                    heapq.heappush(minHeap,(w1 + w2, node2))

        return t if len(visit) == n else -1


     # TC 