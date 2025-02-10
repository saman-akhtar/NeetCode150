class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.v1 = v1
        self.v2 = v2
        self.q = deque()
        if v1:
            self.q.append((self.v1, 0))
        if v2:
            self.q.append((self.v2, 0))
        # Time Complexity: O(1) since only two lists are processed.
        

    def next(self) -> int:
        if not self.hasNext():
            raise StopIteration("no more elements")
        arr, index = self.q.popleft()
        val = arr[index]
        if index + 1 < len(arr):
            self.q.append((arr, index + 1))
      
        return val

    

    def hasNext(self) -> bool:
        return ( self.q)


        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())

# TC 

# SC 


# Operation	Time Complexity	Space Complexity
# Initialization	
# \U0001d442
# (
# 1
# )
# O(1)	
# \U0001d442
# (
# \U0001d43e
# )
# O(K)
# next()	
# \U0001d442
# (
# 1
# )
# O(1)	
# \U0001d442
# (
# \U0001d43e
# )
# O(K)
# hasNext()	
# \U0001d442
# (
# 1
# )
# O(1)	
# \U0001d442
# (
# 1
# )
# O(1)
# Total (for N elements)	
# \U0001d442
# (
# \U0001d441
# )
# O(N)	
# \U0001d442
# (
# \U0001d43e
# )
# O(K)