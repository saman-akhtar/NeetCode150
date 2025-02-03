class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
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


        # MEMOIZATION
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
        # SC O(M * N) + O(N)