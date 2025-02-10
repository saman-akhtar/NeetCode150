# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import heapq
from typing import List
class MergingIterator:
    def __init__(self, iterators):
        # self.q= deque()
        self.lists = iterators
        self.indices = [0] * len(self.lists)
        self.heap = []
        for i,lists in enumerate(iterators):
            if lists:
                heapq.heappush(self.heap, (lists[0], i))
                
            
            
    def hasNext(self):
	    return bool(self.heap)
	    
    def  next(self):
        if not self.hasNext():
	        return StopIteration("No list present")
        val, index = heapq.heappop(self.heap)
        self.indices[index] += 1
        if self.indices[index] < len(self.lists[index]) :
            heapq.heappush(self.heap, (self.lists[index][self.indices[index]] , index))
        return val
	   
	   
lists = [[1, 4, 7], [2, 5, 8, 11], [3, 6, 9, 12]]
merged_iterator = MergingIterator(lists)

result = []
while merged_iterator.hasNext():
    result.append(merged_iterator.next())

print(result)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12]
	    
