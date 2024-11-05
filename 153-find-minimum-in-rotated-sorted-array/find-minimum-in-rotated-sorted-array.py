class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        
        while l < r:
            m = (l + r) // 2
            
            # If the middle element is greater than the rightmost element,
            # the minimum is in the right half
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        # The loop ends when l == r, which is the index of the smallest element
        return nums[l]
        # l ,r = 0 , len(nums)-1
        # while l <= r:
        #     m = (l+ r)//2
        #     print("m", m, len(nums))
        #     # check for range
        #     if (m in rangenums[m-1] > nums[m] and nums[m+1]> nums[m] ):
        #         return nums[m]
        #     elif (m  < len(nums) and nums[m+1] < nums[m]):
        #         l = m+1
        #     else:
        #         r = m -1
        # return nums[0]
            
        