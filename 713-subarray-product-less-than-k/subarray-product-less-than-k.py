class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if not nums or k == 0:
            return 0
        l = 0
        product = 1
        subarray = 0
        for r in range(len(nums)):
            product = product * nums[r]
            # EDGE CASE
            while product >= k and l <= r:
                product = product // nums[l]
                l += 1
            
            subarray += (r - l + 1)
        return subarray if subarray > 0 else 0

        # O(N)
        # SC O(1)

                
        
        