class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        h = len(nums) -1
        while l < h:
            m = (l +h)//2
            if nums[m] > nums[h]:
                l = m + 1
            else:
                h = m
        return nums[l]












        # l, r = 0, len(nums) - 1
        
        # while l < r:
        #     m = (l + r) // 2
            
        #     # If the middle element is greater than the rightmost element,
        #     # the minimum is in the right half
        #     if nums[m] > nums[r]:
        #         l = m + 1
        #     else:
        #         # We use r = m to include the middle element in our search range when there’s a possibility that it could be the minimum.
        #         r = m
        
        # # The loop ends when l == r, which is the index of the smallest element
        # return nums[l]
# Time Complexity: \U0001d442(log\U0001d45b)
# O(logn), since we are using binary search.
# Space Complexity: 
# \U0001d442(1)
# O(1), as we are using a constant amount of space.





