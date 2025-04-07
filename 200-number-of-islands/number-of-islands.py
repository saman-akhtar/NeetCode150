class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        

        # DFS
        if not grid:
            return 0
        ROW,COL = len(grid), len(grid[0])
        visit = set()
        no_island = 0
        def dfs(r,c):
            # no_island += 1 wrong to inc here, as dfs called for each cell it will just inc
            visit.add((r,c))
            dir = [[1,0],[0,1],[0,-1],[-1,0]]
            for r1,c1 in dir:
                
                row = r1 + r
                col = c1 + c
                if ((row,col) not in visit and row in range(ROW) and col in range(COL) and grid[row][col] == "1") :
                    dfs(row,col)
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1" and (r,c) not in visit:
                    dfs(r,c)
                    no_island += 1 
        return no_island

        # O(n *m)
#         Time Complexity: 

# O(m×n)
# Each "1" cell is visited only once due to the visited set, ensuring no cell is processed multiple times.

# Space Complexity: 
# O(m×n)
# Due to the visited set and potential recursion stack depth in the worst-case scenario.

# visited once , but check 5 time 1 in first dfs loop & 4 for dir .. but constant doest contribite to tc
        