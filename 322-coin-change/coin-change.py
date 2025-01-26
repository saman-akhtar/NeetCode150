class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 12 2 2 2 2 
        # MEMOIZATION

        memo = {}
        n = len(coins)
        def dp(i, amt):
            if i < 0 or amt < 0:
                return float('inf')
            if amt <= 0 :
                return 0
            
            if (i,amt) in memo:
                return memo[(i,amt)]
            # check for capacity, 
            # if withn capcity: u have optionto choose or discard
            if ( coins[i] <= amt):
                inc = 1 + dp(i , amt - coins[i])
                exc = dp(i - 1, amt)
                memo[(i, amt)] = min(inc,exc)
                return memo[(i, amt)]
            else:
                # cur coin > amt, then exculude
                memo[(i, amt)] = dp(i-1,amt)
            return memo[(i, amt)]
        
        
        min_len = dp(n-1, amount)
        return -1 if min_len == float('inf') else min_len

        # Approac
        
    #   TC (n×amount)

    #   SC O(n×amount)= O(n×amount) (for memoization table) +O(n) (for recursion stack) 


       # Approach 1
    #    self.minmt = float('inf')
    #     def findMin(i, no ,amt):
            
    #         if i == len(coins):
    #             return self.minmt
            
    #         if amt >  amount:
    #             return self.minmt
    #         if amt == amount:
    #             self.minmt = min(self.minmt,no)
    #             return self.minmt
    #         inc = float('inf')
    #         if ( i < len(coins)):
    #             inc = findMin (i , no + 1, amt + coins[i])
            
    #         exc = findMin (i + 1 , no , amt )

    #         return min( inc, exc)
    #     self.minmt = findMin( 0 , 0, 0)
    #     return -1 if self.minmt == float('inf') else self.minmt
            # TC s:O(2 ^n)
            # SC 


        