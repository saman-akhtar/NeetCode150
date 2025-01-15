class Solution:
    def maximumProduct(self, nums: List[int]) -> int:

        # # Appproach 1

        # # TC O (Nlogn)
        # # O(1)
        # nums.sort()
        # return max( nums[0] * nums[1]* nums[-1], nums[-1] * nums[-2] * nums[-3])
        max1 = max2 = max3 = float('-inf')
        min1 = min2 = float('inf')
        for num in nums:
            if num > max1:
                max1, max2, max3 = num, max1, max2
            elif num > max2:
                max2, max3 = num, max2
            elif num > max3:
                max3 = num
            
            if num < min1:
                min1, min2 = num, min1
            elif num < min2:
                min2 = num
        return max(min1 * min2 * max1, max1* max2* max3)
                 

# Tes case all pso9v top 3
# all negavtive top3 
# 2  negativ 1  positve

# 2 case
# all max 3 
# 2 sammalled 1 lar
