class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def dp(i, cur_amt):
            if cur_amt == 0:
                return 1
            if ( i < 0 or cur_amt < 0):
                return 0 # inf
            
            if (i,cur_amt) in memo:
                return memo[(i, cur_amt)]

            if coins[i] <= cur_amt:
                memo[(i, cur_amt)] = dp(i -1, cur_amt) + dp(i, cur_amt -coins[i])
            else:
                memo[(i, cur_amt)] = dp(i -1, cur_amt)
            return  memo[(i, cur_amt)] 

        n = len(coins)
        return dp(n-1, amount)
        