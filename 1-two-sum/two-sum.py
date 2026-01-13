class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, n in enumerate(nums):
            diff = target -n
            if diff in d:
                return [d[diff],i]
            else:
                d[n]= i



        # nums.sort()
        # l = 0
        # r = len(nums)-1
        # while l < r:
        #     summ = nums[l]+ nums[r]
        #     if summ == target:
        #         return [l, r]
        #     elif summ > target:
        #         r -= 1
        #     else:
        #         l +=1
        # return [0,0]

