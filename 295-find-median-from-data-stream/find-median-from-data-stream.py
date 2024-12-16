class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap, -1 * num)
        
        # Condition 1 all elemnt in min heap shoul eb greater tahn all in min heap
        if(self.maxHeap and self.minHeap and self.maxHeap[0] * -1 > self.minHeap[0]):
            val = -1 * heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, val)
        # Condition2 : uneven size
        if(len(self.maxHeap) > len(self.minHeap) + 1):
            val = -1 * heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, val)

        if(len(self.minHeap) > len(self.maxHeap) + 1):
            val = -1 * heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, val)
            
        

    def findMedian(self) -> float:
        if( len(self.minHeap) > len(self.maxHeap)):
            return self.minHeap[0]
        if( len(self.maxHeap) > len(self.minHeap)):
            return -1 *self.maxHeap[0]
        return  (-1 *self.maxHeap[0] + self.minHeap[0]) / 2


        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()