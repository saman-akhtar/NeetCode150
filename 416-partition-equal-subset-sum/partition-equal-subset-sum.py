class Solution:

   
    def canPartition(self, nums: List[int]) -> bool:

        #  # can be broken in to target SUm
        # IT IS variation of 0/1 knapsack
        # Approach 1: Bottom up 
        totalSum = sum(nums)
        if totalSum % 2 != 0:
            return False
        target = totalSum//2
        n = len(nums)
        dp = [[False] * (target + 1) for _ in range(n + 1)]
        # base case
        for i in range(n+1):
            dp[i][0]= True
        for i in range(1,n +1):
            for j in range( 1,target + 1):
                if nums[i-1] <= j:
                    dp[i][j] = dp[i-1][j- nums[i-1]] or dp[i-1][j] 
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n][target]

        # TC 
         # APPROACH 2 : Memoization TOp DOWN
        

        # if total sum is odd cant be partion !!!
        totalSum = sum(nums)
        if totalSum % 2 != 0:
            return False
        target = totalSum//2
        memo = {}
        def canBreak(i, cur_sum):
            if cur_sum == 0:
                return True
            if i <= 0:
                return False
            if (i, cur_sum) in memo:
                return memo[(i, cur_sum)]
            # Option 1: include nums[i-1]
        # Option 2: exclude nums[i-1]
            if nums[i-1] <= cur_sum:
                memo[(i, cur_sum)] =canBreak(i-1, cur_sum- nums[i-1]) or canBreak(i-1, cur_sum)
            else:
                memo[(i, cur_sum)]  = canBreak(i-1, cur_sum)


            
            return memo[(i, cur_sum)]
        n = len(nums)
        return canBreak(n, target)
# Type	0/1 Knapsack
# Goal	Can we pick items to sum to total/2
# State	canBreak(i, cur_sum)
# Base Case	cur_sum == 0 → True, i == 0 → False
# Transition	Include or exclude nums[i-1]
# Time Complexity	
# O(n⋅target)
# Space Complexity	

# O(n⋅target) (memo)

        # TC O( n.target)
        # SC 

        # 5  3, 6 ||. 3,11
        # 11      ||  2 0
        