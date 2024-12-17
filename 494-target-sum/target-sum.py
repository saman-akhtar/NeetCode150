class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # # APPROACH 2
        dp = {}

        def dpfunc(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            if( (i,total ) in dp):
                return dp[(i,total)]
            dp[(i,total)] = dpfunc(i +1, total + nums[i]) + dpfunc(i +1, total - nums[i])
            return dpfunc(i,total)
        return dpfunc(0,0)
            
# TC n * t
# SC O( N * T)Where 
# n is the length of the array 
# nums and t is the sum of all the elements in the array.


        # # APPROACH 1


        # count = 0

        # def backtrack(i, total):
        #     nonlocal count

        #     # if total == target:
        #     #     count += 1
        #     #     return 
        #     if i >= len(nums):
        #         if total == target:
        #             count += 1
        #         return
            
        #     #add
        #     backtrack(i + 1, total + nums[i])

        #     #subrtact
        #     backtrack(i + 1, total - nums[i])
        #     return
        # backtrack(0, 0)
        # return count

        # TC 2 ^ n
        # SC O(N)