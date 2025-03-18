class Solution:
    def rob(self, nums: List[int]) -> int:

        # MEMOIZATION
        memo ={}
        def find_amt (n):
            if n == 0:
                return 0
            if n < 0:
                return 0
            if n in memo:
                return memo[n]
            choose = nums[n-1]+ find_amt(n-2)
            nchoose =  find_amt(n-1)
            memo[n] = max(choose, nchoose )
            return memo[n]
        n = len(nums)
        return find_amt(n )
        # TC O(n)
        # SC ON

        # RECURSION
        def find_amt (n):
            if n == 0:
                return 0
            if n < 0:
                return 0
            choose = nums[n-1]+ find_amt(n-2)
            nchoose =  find_amt(n-1)
            maxamt = max(choose, nchoose )
            return maxamt
        n = len(nums)
        return find_amt(n )
        # TC O(2^n)
        # SC ON
    

        