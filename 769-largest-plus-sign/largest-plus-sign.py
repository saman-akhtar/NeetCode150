class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        # approach brute forec

        # go through each cell N2
        # how long is the arm O(N)

        #APPRACH 2
        # we can optimze the pat how long is cell
        # if we take single row.. min v1 order value for any cell
        # min(left,right) .. if we see the relationship
        # we find i overlapp.. so instead we cand min 1 on left of each arm & min no of 1 
        # on right of each arm

        # SC - O(n^2); as we have to build the grid

        grid = [[inf]* n for i in range(n)]

        for (x,y) in mines:
            grid[x][y] = 0

        for i in range(n):
            left = 0
            for j in range(n):
                left += 1
                if ( grid[i][j]==0):
                    left = 0
                else:
                    grid[i][j]=min(grid[i][j],left)

            right = 0
            for j in reversed(range(n)):
                right += 1
                if ( grid[i][j]==0):
                    right = 0
                else:
                    grid[i][j]=min(grid[i][j],right)
        for i in range(n):
            left = 0
            for j in range(n):
                left += 1
                if ( grid[j][i]==0):
                    left = 0
                else:
                    grid[j][i]=min(grid[j][i],left)

            right = 0
            for j in reversed(range(n)):
                right += 1
                if ( grid[j][i]==0):
                    right = 0
                else:
                    grid[j][i]=min(grid[j][i],right)
        final_ans = -inf
        for row in grid:
            for x in row:
                final_ans = max(final_ans,x)
        return final_ans