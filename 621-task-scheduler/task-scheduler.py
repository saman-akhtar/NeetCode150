class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        q = deque()
        heap =[]
        for v in count.values():
            heapq.heappush(heap, -v)
        t = 0
        while heap or q:
            
            t += 1
            if heap:
                cur = heapq.heappop(heap)
                rem = cur + 1
                if( rem < 0):
                    q.append((rem, t + n ))
                    
            if  q and q[0][1] == t:
                res = q.popleft()
                heapq.heappush(heap,res[0] )
        return t
