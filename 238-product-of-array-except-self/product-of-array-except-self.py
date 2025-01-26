class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        
        # 1,  2,  3, 4
        # 1   1   2  6
        # 24  12  4  1 
        # 24. 12.  8 6
        left_prod = [1] *len(nums)
        right_prod= [1] *len(nums)
        res = [1] *len(nums)
        for i in range(1, len(nums)):

            res[i] = res[i-1] * nums[i-1]

        for i in (range(len(nums)-2, -1, -1)):
            right_prod[i] = right_prod[i+1] * nums[i+1]

        for i in range(len(nums)):
            res[i]= res[i]* right_prod[i] 
        return res