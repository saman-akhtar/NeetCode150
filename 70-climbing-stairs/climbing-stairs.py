class Solution:
    def climbStairs(self, n: int) -> int:
        # dp = [0] * (n+1)
        # dp[1] = 1

        # # bottom up approach
        # if n == 1:
        #     return 1
        # dp[2] = 2
        # for i in range(3, len(dp)):
        #     dp[i] = dp[i-2] + dp[i-1]
        # return dp[n]
       
       # TC O(N)
       # SC O(N)

    # optimized
        prev1 = 1
        prev2 = 2
        if n == 1:
            return 1
        if n == 2:
            return 2
        for i in range(3, n+1):
            cur = prev1 + prev2
            prev1 = prev2
            prev2 = cur
        return prev2
    # TC O(n)
    # SC O(1)

    #recir app :Time Complexity: O(2 ^n)
