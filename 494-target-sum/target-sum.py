class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # bottom UP
        memo = {}
        total_sum = sum(nums)
        if (total_sum + target) % 2 != 0 or total_sum < abs(target):
            return 0
        new_target = (total_sum + target) // 2
        def findTarget(i, cur_sum):
            
            # if i == -1 and cur_sum == new_target:
            #     return 1
            if i == -1:
                if cur_sum == 0:
                    return 1
                return 0
            
            if ( i, cur_sum) in memo:
                return memo[(i,cur_sum)]
            if nums[i] <= cur_sum:
            
                memo[(i,cur_sum)] = findTarget(i-1, cur_sum - nums[i])+ findTarget(i -1, cur_sum)
            else:
                memo[(i,cur_sum)] = findTarget(i -1, cur_sum )
            return memo[(i,cur_sum)]
        
        n = len(nums)
        nw = findTarget(n-1, new_target)
        return nw


        # # # APPROACH 2
        # dp = {}

        # def dpfunc(i, total):
        #     if i == len(nums):
        #         return 1 if total == target else 0
        #     if( (i,total ) in dp):
        #         return dp[(i,total)]
        #     dp[(i,total)] = dpfunc(i +1, total + nums[i]) + dpfunc(i +1, total - nums[i])
        #     return dpfunc(i,total)
        # return dpfunc(0,0)
            
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