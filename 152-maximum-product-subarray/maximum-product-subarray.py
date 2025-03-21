class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res = nums[0]
        curMax = 1
        curMin = 1
        for n in nums:
            # if n == 0:
            #     continue
            oldMax = curMax * n
            curMax = max(curMax * n , curMin * n, n)
            curMin = min(oldMax , curMin * n, n)
            res = max(res, curMax)
        return res
        def findMax(i, prev):
            # no profuct from nothung ?
            if i == 0:
                return float(-inf)
            
            choose = max( nums[i-1] ,findMax(i -1, nums[i-1] ))
            notchoose = max( prev * nums[i-1] ,findMax(i -1, 1))
            return max(choose, notchoose)
        n = len(nums)
        return findMax(n, 1)

        #     2 0 1
        #     1
        #   1. 10