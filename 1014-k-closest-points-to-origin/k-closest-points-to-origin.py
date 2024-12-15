class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        d = [(-1 *(i[0] **2 + i[1] **2), i) for i in points]
        
        heapq.heapify(d)
        res = []
        # for i in range(k):
        while len(d) > k:
            heapq.heappop(d)
        d = [i[1] for i in d]
        return d 
        
