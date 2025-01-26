class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.minmt = float('inf')
        memo = {}
        def findMin(i,  amt):
            
            if amt == 0:
                return 0
            if amt < 0 or i == len(coins):
                return float('inf')

            if (i,amt) in memo:
                return memo[(i,amt)]
           
            # Option 1: Include the current coin
            include = 1 + findMin(i, amt - coins[i])

            # Option 2: Exclude the current coin
            exclude = findMin(i + 1, amt)

            memo[(i, amt)] = min(include, exclude)
            return memo[(i, amt)]

        self.minmt = findMin( 0 ,  amount)
        return -1 if self.minmt == float('inf') else self.minmt
      
            


        