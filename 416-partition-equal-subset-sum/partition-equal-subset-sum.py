class Solution:

    # APPROACH 3
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        if totalSum % 2 != 0:
            return False
        target =totalSum //2
        
        dp = set()
        dp.add(0)
        for i in range(len(nums)-1,-1,-1):
            nextDP = set()
            for t in dp:
                nextDP.add(t + nums[i])
                # get old data
                nextDP.add(t)
            dp = nextDP
        if target in dp:
            return True
        return False


    # Claryfying
    # can there be negative no
    # Apaprch 2
    # def canPartition(self, nums: List[int]) -> bool:
    #     totalSum = sum(nums)
    #     if totalSum % 2 != 0:
    #         return False

    #     target = totalSum // 2
    #     memo = {}
    #     def backtrack(i, sums):
    #         if sums == target:
    #             return True
    #         # If we've gone beyond the array or exceeded the target, no valid partition exists
    #         if i >= len(nums) or sums > target:
    #             return False

    #         if( i,sums) in nums:
    #             return memo[(i, sums)]
    #         include = backtrack(i + 1, sums + nums[i])
    #         exclude = backtrack(i + 1, sums)

    #         # Cache the result for this state
    #         memo[(i, sums)] = include or exclude
    #         return memo[(i, sums)]
    #     return backtrack(0, 0)

    # TC O(n⋅target):
    # SC O(n⋅target). target: The target sum to check (half of the total sum).

    
    #if there exists a subset whose sum equals half of the total sum of the array. A two-poi
    # def canPartition(self, nums: List[int]) -> bool:
    #     ts = sum(nums)
    #     target = ts /2

    #     # Approach 1
    #     def backtrack(i, sums):
    #         if sums == target:
    #             return True
    #         if i >= len(nums):
    #             return False
    #         res1 = backtrack(i + 1, sums + nums[i])
    #         res2 = backtrack(i + 1, sums )
    #         return res1 or res2
    #     return backtrack(0, 0)
        # TC O(2 ^n)

        