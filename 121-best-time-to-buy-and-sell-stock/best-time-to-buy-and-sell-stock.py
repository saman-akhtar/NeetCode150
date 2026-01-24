class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = l +1
        n = len(prices)
        p = 0
        for r in range(1,n):
            if prices[l] < prices[r]:
                cp = prices[r] - prices[l]
                p = max(cp, p)
            else:
                l = r

        return p

                