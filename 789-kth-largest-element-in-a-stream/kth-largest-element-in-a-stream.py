class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = nums
        heapq.heapify(self.minHeap) # ON
        while len(self.minHeap) > k:  #O (K) +> OK(Klogn)
            heapq.heappop(nums) # O(logn)
        
        

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap,  val) #O(logn)
        while len(self.minHeap) > self.k: #O(logK)
            heapq.heappop(self.minHeap)

        return self.minHeap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)


# TC
# _init = O(n) + O(logN) * (n-k)= O(nlogn).
# add O(logk) * m .. heap take log k as heap size is atmost k, m add operation

#space
# O(k) .. at max stores k elemets

        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)