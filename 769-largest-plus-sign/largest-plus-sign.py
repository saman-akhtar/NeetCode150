class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        # approach brute forec

        # go through each cell N2
        # how long is the arm O(N)
        # # Step 1: Initialize the grid with 1s
        # grid = [[1] * n for _ in range(n)]
        
        # # Step 2: Mark all cells in mines as 0
        # for r, c in mines:
        #     grid[r][c] = 0
        
        # # Step 3: Initialize the maximum order
        # max_order = 0
        
        # # Step 4: Brute-force to compute the largest plus sign for every cell
        # for i in range(n):
        #     for j in range(n):
        #         if grid[i][j] == 0:
        #             continue  # Skip if the cell is part of a mine
                
        #         # Check the size of the plus sign centered at (i, j)
        #         order = 0
        #         while (
        #             i - order >= 0 and i + order < n and
        #             j - order >= 0 and j + order < n and
        #             grid[i - order][j] == 1 and
        #             grid[i + order][j] == 1 and
        #             grid[i][j - order] == 1 and
        #             grid[i][j + order] == 1
        #         ):
        #             order += 1
                
        #         # Update the maximum order found so far
        #         max_order = max(max_order, order)
        
        # return max_order


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