class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        # res = nums[0]
        # curMax = 1
        # curMin = 1
        # for n in nums:
        #     # if n == 0:
        #     #     continue
        #     oldMax = curMax * n
        #     curMax = max(curMax * n , curMin * n, n)
        #     curMin = min(oldMax , curMin * n, n)
        #     res = max(res, curMax)
        # return res
        def dfs(i, curMax, curMin, overall):
            # When we've processed all elements, return overall.
            if i == len(nums):
                return overall
            cur = nums[i]
            # Calculate new maximum and minimum products ending at index i.
            newMax = max(cur, cur * curMax, cur * curMin)
            newMin = min(cur, cur * curMax, cur * curMin)
            newOverall = max(overall, newMax)
            return dfs(i + 1, newMax, newMin, newOverall)
        
        # Start recursion from index 1, initializing with the first element.
        return dfs(1, nums[0], nums[0], nums[0])
        def dfs(i, curMax, curMin, overall):
            # Base case: when i == 0, we have processed all elements.
            if i == 1:
                return abs(nums[0])
            # Get the current element.
            cur = nums[i-1]
            # Calculate the maximum product ending at the current element.
            newMax = max(cur, cur * curMax, cur * curMin)
            # Calculate the minimum product ending at the current element.
            newMin = min(cur, cur * curMax, cur * curMin)
            # newOverall here is computed as the maximum of the current value and newMax.
            newOverall = max(cur, newMax)
            # Recurse by moving one step backward.
            return dfs(i - 1, newMax, newMin, newOverall)
        n = len(nums)
        return dfs(n, nums[n-1],nums[n-1], nums[n-1])


        # tc O(n)
        # Space Complexity: O(n) due to the recursion stack

        #     2 0 1
        #     1
        #   1. 10