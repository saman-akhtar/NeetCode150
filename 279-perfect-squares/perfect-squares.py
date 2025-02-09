class Solution:
    def numSquares(self, n: int) -> int:
        #     0   0  0. 0 0
#     1   0 1   2   3
#     2   0 inf inf inf
#     3   0
#     4.  0
#     5.  0
        memo = {}
        def dp( cur_n):
            if (cur_n < 0):
                return float('inf')
            if (cur_n == 0):
                return 0
            if ( cur_n) in memo:
               return memo[cur_n]

            min_no = float('inf')
            i = 1
            while i **2 <= cur_n:
                min_no = min (min_no, 1 + dp(  cur_n - (i) **2))
                i += 1
            memo[ cur_n] = min_no
            return memo[cur_n]
        return dp( n)


        # def dp( i, cur_n):
        #     if (cur_n < 0):
        #         return float('inf')
        #     if (cur_n == 0):
        #         return 0

        #     min_no = float('inf')
        #     i = 1
        #     while i **2 <= cur_n:
        #         min_no = min (min_no, 1 + dp( i , cur_n - (i) **2))
        #         i += 1

        #     return min_no
        # return dp( n, n)

        # TC 
        # SC

            