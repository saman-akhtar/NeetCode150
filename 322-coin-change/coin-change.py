class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # DP :top down
        # n = len(coins)
        # dp = [[float("inf")]*(amount + 1) for i in range(n+ 1)]
        # for i in range(n +1):
        #     dp[i][0]=  0

        # for i in range(1,n + 1):
        #     for j in range(1, amount + 1):

        #         if coins[i-1] <= j:
        #             dp[i][j]= min(dp[i-1][j], 1 + dp[i][j - coins[i-1]])
        #         else:
        #             dp[i][j]= dp[i-1][j]
        # return dp[n][amount] if dp[n][amount] != float('inf') else -1
        # # TC O(N)
        # SC O(1)

        # approach 2 memoization
        # DP bottom up
        memo = {}
        def find_min_amt(i, amt):
            if i <= 0 or amt < 0:
                return float('inf')
            if amt == 0 :
                return 0
            

            if (i,amt) in memo:
                return memo[(i,amt)]
            # if coins[i-1]
            if coins[i-1] <= amt:
                res = min(1 + find_min_amt(i, amt-coins[i-1]), find_min_amt(i-1, amt))
            else:
                res = find_min_amt(i-1, amt)
            memo[(i,amt)]= res
            return res
        n = len(coins)
        result = find_min_amt(n, amount)
        return result if result != float('inf') else -1
        # 12 2 2 2 2 
        # MEMOIZATION

                #code here
#         0  1      2.    3.  ammt
#     0   0  -inf.  -inf -inf
#     1   0  0  2 3
#     2   0
#     3   0
#     4.  0
#     5.  0
# coins


        # boottom up 
        # WHY?
        # less space
        # you build base case and then end result
        n = len(coins)
        dp = [[float(inf)]* (amount + 1) for _ in range(len(coins) + 1)]
        # base case
        
        for i in range(n + 1):
            dp[i][0] = 0  
        for i in range(1,len(coins) + 1):
            for j in range(1, (amount + 1)):
                if (coins[i-1] <= j):
                    dp[i][j]  = min(dp[i-1][j], 1 + dp[i][j- coins[i-1]])
                else:
                    dp[i][j] = dp[i-1][j]
        return -1 if dp[n][amount] == float('inf') else dp[n][amount]
        # TC =  O(n×amount)
        # SC recursive = O(n×amount) only for string 2d We use a (n+1) x (amount+1) matrix.
       



        # memo = {}

        # def dp(i, cur_amt):
            
        #     if cur_amt == 0 :
        #         return 0
        #     if i < 0:
        #         return float('inf') 
        #     if (i,cur_amt) in memo:
        #         return memo[(i,cur_amt)]
        #     exc = dp(i -1, cur_amt )
        #     inc = float('inf') 
        #     if coins[i] <= cur_amt:
        #        inc = 1 + dp(i, cur_amt - coins[i])
        #     # else:
        #     min_coins = min(exc, inc)
        #     memo[(i,cur_amt)] = min_coins
        #     return memo[(i,cur_amt)]

        # n = len(coins) - 1
        # min_coins = dp(n, amount)
        # return -1 if min_coins == float('inf') else min_coins
        # TC o (n * amt)
        # SC recursive = O(n×amount)+O(amount) . O(amount becuasde of recusive sapce)
        # TOP down ? u first fill end result in recursive pathe go to end of branch 

        def dp(i, cur_amt):
            
            if cur_amt == 0 :
                return 0
            if i < 0:
                return float('inf') 
            exc = dp(i -1, cur_amt )
            inc = float('inf') 
            if coins[i] <= cur_amt:
               inc = 1 + dp(i, cur_amt - coins[i])
            # else:
            min_coins = min(exc, inc)
            return min_coins

        n = len(coins) - 1
        min_coins = dp(n, amount)
        return -1 if min_coins == float('inf') else min_coins
        # TC 2 ^ (n + amt)
        # SC recursive = O(amount)
        # What is the maximum depth the recursion can go?
        # In coin change, the deepest path is choosing the smallest coin repeatedly.
        # Depth = amount in the worst case.
        




        # memo = {}
        # n = len(coins)
        # def dp(i, amt):
        #     if i < 0 or amt < 0:
        #         return float('inf')
        #     if amt <= 0 :
        #         return 0
            
        #     if (i,amt) in memo:
        #         return memo[(i,amt)]
        #     # check for capacity, 
        #     # if withn capcity: u have optionto choose or discard
        #     if ( coins[i] <= amt):
        #         inc = 1 + dp(i , amt - coins[i])
        #         exc = dp(i - 1, amt)
        #         memo[(i, amt)] = min(inc,exc)
        #         return memo[(i, amt)]
        #     else:
        #         # cur coin > amt, then exculude
        #         memo[(i, amt)] = dp(i-1,amt)
        #     return memo[(i, amt)]
        
        
        # min_len = dp(n-1, amount)
        # return -1 if min_len == float('inf') else min_len

        # Approac
        
    #   TC (n×amount)

    #   SC O(n×amount)= O(n×amount) (for memoization table) +O(n) (for recursion stack) 


       # Approach 1
    #    def coinChange(self, coins: List[int], amount: int) -> int:
        # n = len(coins)

        # def dp(i, amt):
        #     # Base cases
        #     if i < 0 or amt < 0:  # No more coins or invalid amount
        #         return float('inf')
        #     if amt == 0:  # Exact amount achieved
        #         return 0

        #     # Recursive cases
        #     if coins[i] <= amt:
        #         # Include the current coin
        #         inc = 1 + dp(i, amt - coins[i])
        #         # Exclude the current coin
        #         exc = dp(i - 1, amt)
        #         return min(inc, exc)
        #     else:
        #         # Exclude the current coin
        #         return dp(i - 1, amt)

        # # Start recursion with the last coin and the full amount
        # min_len = dp(n - 1, amount)
        # return -1 if min_len == float('inf') else min_len
            # TC s:O(2^(n + m))    
            # SC  o(M)


        