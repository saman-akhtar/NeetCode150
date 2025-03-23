class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        # UNBOUND KNAPSAKC
        # Bottom up
        n = len(coins)

        dp = [[0] * (amount + 1) for _ in range(n +1)]
        # 0 amount , no of way 1
        # 0 coins 
        for i in range(n+1):
            dp[i][0]= 1
        for i in range(1,n+1):
            for j in range(1,amount+1):
                if coins[i-1] <= j:
                    dp[i][j]=  dp[i][j-coins[i-1]]+ dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[n][amount]
        # TC O( N * Amount)
        # SC O( N * Amount)






        memo = {}

        def dp(i, cur_amt):
            if cur_amt == 0:
                return 1
            if ( i < 0 or cur_amt < 0):
                return 0 
            
            if (i,cur_amt) in memo:
                return memo[(i, cur_amt)]

            if coins[i] <= cur_amt:
                memo[(i, cur_amt)] = dp(i -1, cur_amt) + dp(i, cur_amt -coins[i])
            else:
                memo[(i, cur_amt)] = dp(i -1, cur_amt)
            return  memo[(i, cur_amt)] 

        n = len(coins)
        return dp(n-1, amount)

# TC O(N * amyt)
# SC O(N * amt)  + O(N)
        