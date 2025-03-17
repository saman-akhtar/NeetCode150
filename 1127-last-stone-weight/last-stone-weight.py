class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        new_stones = [-1 * stone for stone in stones]
        heapq.heapify(new_stones)
        while new_stones:
            stone1 = heapq.heappop(new_stones)
            if new_stones:
                stone2 = heapq.heappop(new_stones)
            else:
                return abs(stone1)
            diff = abs(stone1 -stone2)
            if diff > 0:
                heapq.heappush(new_stones, -diff)
        return 0 if len(new_stones) == 0 else abs(new_stones[0])










        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            y = heapq.heappop(stones)
            x = heapq.heappop(stones)
            if ( x != y):
                heapq.heappush(stones, ((y-x)))
            
        if len(stones) == 0:
            return 0
        return abs(stones[0])
# TC n + n * logn
# SC ON
        