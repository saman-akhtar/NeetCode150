class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        l = 0
        for r in range(n):
            if nums[r] != 0 :
                nums[l],nums[r] = nums[r],nums[l]
                l += 1
        # TC O(N)
        # SC O(1)
        
            
                
        # 0 0 1 2
        # l r r
        # 1 0 0 2
        #    l   r
        # 0 1 0 2
        # 1 0
        #   l r
        # 0 1 2 0
        # 1 0 2 0
        #   2 0
        # 1 0 3 0
        
        
        # n = len(nums)
        # arr = [0] * n
        # j = 0
        # for i in range(n):
        #     if nums[i] != 0:
        #         arr[j] = nums[i]
        #         j += 1
        # nums[:] = arr