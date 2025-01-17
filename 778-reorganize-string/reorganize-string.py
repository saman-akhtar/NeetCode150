class Solution:
    def reorganizeString(self, s: str) -> str:
        wmap = Counter(s)
        maxheap = [[-v,k]for k, v in wmap.items()]
        heapq.heapify(maxheap) #O(N)
        prev = None
        s = ""
        while maxheap or prev:
            if prev and not maxheap:
                return ""
            if maxheap:
                cnt, val = heapq.heappop(maxheap)
                s += val
                cnt += 1
            if prev:

                heapq.heappush(maxheap, prev)
                prev = None
            if cnt < 0:
                prev = [cnt,val]
        return s


