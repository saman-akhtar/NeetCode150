class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # UNBOUND KNAPSAKC
        # Bottom up

        dp = [[0] * (n + 1) for _ in range(m +1)]
        # 0 amount , no of way 1
        # 0 coins 
         # Base case: the closer to desination is 1
        # bottom + right
        dp[m-1][n-1] =1
        # dp[m-1][n-2] =1
        # dp[m-2][n-1] =1
        print("DP", dp)
        # for i in range()
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i + 1 < m:
                    # bottom
                    dp[i][j]+= dp[i+1][j]
                if j +1 < n:
                    dp[i][j] += dp[i][j+1]
        return dp[0][0]
        #Time: O(m × n)
        #Space: O(m × n)

#    0 1 2
#  0 0 0 0 
#  1 0 1 0
#  2 1 1 0.    m[2][1]  m[2][0] m[1][1].    m[i-1][j-2]. m[i-2][j-1]
#  3 0 0 0

#    0 1 2
#  0 3 1 0 
#  1 2 1 0
#  2 1 1 0.    m[2][1]  m[2][0] m[1][1].    m[i-1][j-2]. m[i-2][j-1]
#  3 0 0 0
        # DP 
        grid = [[0] * n for i in range(m)]
        for i in range(m):
            grid[i][n-1] =1

        
        for j in range (n):
            grid[m-1][j] =1
        
        for row in range(m-2,-1,-1):
            for col in range(n-2,-1,-1):
                grid[row][col]=grid[row+1][col]+grid[row][col+1]
        return grid[0][0]

         # Bottom up:from the bottom-right to the top-left computing the solution step by step.


        # TC O(N * M)
        # SC O(N * M)


        # MEMOIZATION

        # TOp DOwn
        # ROWS, COLS = m-1, n-1
        # grid = [[0] * n for i in range(m)]
        # grid[m-1][n-1] = 1
        # memo = {}
        # self.count = 0
        # def dp(i, j):
        #     if i not in range(m) or j not in range(n):
        #         return 0
        #     if grid[i][j] == 1:
        #         return 1
        #     if (i,j) in memo:
        #         return memo[(i,j)]
            
        #     memo[(i,j)] = dp( i, j +1) + dp(i + 1, j)
        #     return memo[(i,j)]
             
        # return dp(0, 0)
        
        # TC O (M * n)
        # SC O(M * N) +  O(m + n) in the worst case.

       