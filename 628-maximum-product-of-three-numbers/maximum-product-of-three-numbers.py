class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        # if len(nums) > 3 and nums[0] < 1 and nums[1] < 1 and ((nums[0] * nums[1]) > (nums[-1] * nums[-2]) or nums[-3] < 1):
            
        #     return nums[0] * nums[1]* nums[-1]

        # return nums[-1] * nums[-2] * nums[-3]
        return max( nums[0] * nums[1]* nums[-1], nums[-1] * nums[-2] * nums[-3])


# Tes case all pso9v top 3
# all negavtive top3 
# 2  negativ 1  positve
