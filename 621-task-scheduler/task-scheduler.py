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
                    q.append((rem, t + n))
                    
            if  q and q[0][1] == t:
                res= q.popleft()
                heapq.heappush(heap,res[0] )
        return t
# TC  O(T⋅logk), where 
# \U0001d447
# T is the total number of tasks (including idle slots), and 
# \U0001d458
# k is the number of unique tasks. Each heap operation takes 
# O(logk).
# SC O(k) for the heap and 

# O(k) for the cooldown queue, where 
# \U0001d458
# k is the number of unique tasks.