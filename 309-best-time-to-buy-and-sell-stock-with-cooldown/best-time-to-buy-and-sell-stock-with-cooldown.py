class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        # BOttom up
        n = len(prices)
        if n <= 1:
            return 0
        dp = [[0]*2 for i in range(n+1)]
        for i in range(n - 1, -1, -1):
            for buying in [True, False]:
                if buying:
                    buy = dp[i + 1][False] - prices[i] if i + 1 < n else -prices[i]
                    cooldown = dp[i + 1][True] if i + 1 < n else 0
                    dp[i][1] = max(buy, cooldown)
                else:
                    sell = dp[i + 2][True] + prices[i] if i + 2 < n else prices[i]
                    cooldown = dp[i + 1][False] if i + 1 < n else 0
                    dp[i][0] = max(sell, cooldown)

        return dp[0][1] # sell day




        # TOP DOWN
        n = len(prices)
        if n <= 1:
            return 0
        # at each step decion by, cooldonw
        # sell ,colldaonw
        # after sell alway cooldown
        memo = {}
        def max_profit(i, buy):
            if i >= len(prices):
                return 0
            if (i,buy) in memo:
                return memo[(i,buy)]
            cooldown = max_profit(i+1, buy)
            if buy:
                profit = max(cooldown, -prices[i] + max_profit(i+1, not buy))
            else:
                profit = max(cooldown, prices[i] + max_profit(i+2, not buy))
            memo[(i,buy)] = profit
            return memo[(i,buy)]


            
        return max_profit(0, True)
        # O(2.n) o (n)
        # SC O(2.n) O(n)
        
        

        # order buy sell , cnat buy again before selling
        # aftser sell 1 day cooldown
        # 1 2 3
        # b   s. 2
        # 1 2 3 7
        # b.    s 6
        # b s c   1
        # b   s c 2

        # 1 7 2 8
        # b s c    6
        # b     s. 7
        #     b s  6

