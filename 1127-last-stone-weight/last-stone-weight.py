class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        nstones = []
        for i in range(len(stones)):
            heapq.heappush(nstones,-1 * stones[i])
        while nstones:
            y= -1 * heapq.heappop(nstones)
            if nstones:
                x=  -1 * heapq.heappop(nstones)
            else:
                return y

            if y > x:
                heapq.heappush(nstones,-1 * (y-x))
        return 0
        new_stones = [-1 * stone for stone in stones]
        heapq.heapify(new_stones)
        while len(new_stones) > 1:
            stone1 = heapq.heappop(new_stones)
            stone2 = heapq.heappop(new_stones)
            diff = abs(stone1 -stone2)
            if diff > 0:
                heapq.heappush(new_stones, -diff)
        return 0 if len(new_stones) == 0 else abs(new_stones[0])








# TC n + n * logn
# SC ON
        