class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            y = heapq.heappop(stones)
            x = heapq.heappop(stones)
            # x = 0
            if ( x != y):
                heapq.heappush(stones, ((y-x)))
            
        if len(stones) == 0:
            return 0
        return abs(stones[0])
        