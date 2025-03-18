class Solution:
    def climbStairs(self, n: int) -> int:

        # DP - top down
        if n == 1:
            return 1
        prev1, prev2 = 1,2
        for i in range(3, n + 1):
            cur = prev2 + prev1
            prev2,prev1 = cur, prev2
        return prev2


        # DP - MEMOZATIOn
        # climb = {}
        # def memo(n):
        
        #     if n == 1:
        #         return 1
        #     elif n == 2: 
        #         return 2
        #     if n in climb:
        #         return climb[n]
        
        #     stair1 =  climb[n-1]  if n -1  in climb else memo(n-1)
        #     stair2 =  climb[n-2] if n -2  in climb else memo(n-2)
        #     climb[n]=  stair1 + stair2
        #     return climb[n]
        
        # return memo(n)
        #TC O(N): Each unique n is computed once and stored in climb
        # SC O(N)(due to memoization dictionary + recursion depth)

        # RECURSION Approach 1
        # if n == 1:
        #     return 1
        # elif n == 2: 
        #     return 2
        # return self.climbStairs(n-1) + self.climbStairs(n-2)
        #. TC O(2 ^n)
        # SC O(N)



        # dp = [0] * (n+1)
        # dp[1] = 1

        # # bottom up approach
        # if n == 1:
        #     return 1
        # dp[2] = 2
        # for i in range(3, len(dp)):
        #     dp[i] = dp[i-2] + dp[i-1]
        # return dp[n]
       
       # TC O(2 ^ N)
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
    # Recursive with Memoization (Top-Down)	
    # TC O(n)
    # SC O(n)
