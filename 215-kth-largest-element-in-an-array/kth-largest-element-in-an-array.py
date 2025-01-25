class Solution:

    # clarifying question : is k valid ? k wont exceed array size

    #
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # APPROACH 1
        # nums = [-1 * i for i in nums]
        # heapq.heapify(nums)
        # largtest = 0

        # while k > 0:
        #     largtest = -1 * heapq.heappop(nums)
        #     k -=1
        # return largtest

# O(n+k⋅logn)
# SC O(N)
        # APPROACH 2
        heap = []
        for i in nums:
            heapq.heappush(heap, i)
            if(len(heap) > k):
                heapq.heappop(heap)
        return heapq.heappop(heap)

       

# TC O Nlog k
# SC O K
            

        