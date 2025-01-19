class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row  = len(grid)
        col  = len(grid[0])
        t = 0
        q = deque()
        fresh  =0

        for r in range(row):
            for c in range(col):
                if (grid[r][c]== 1):
                    fresh += 1
                elif (grid[r][c]== 2):
                    q.append([r,c])
        dirs = [[1,0],[-1,0],[0,-1],[0,1]]
        while q and fresh > 0:
            for i in range(len(q)):
                r,c = q.popleft()
                for dr,dc in dirs:
                        r1 = dr + r
                        c1= dc + c
                        if ( r1 in range(row) and c1 in range(col)  and grid[r1][c1]==1
                        ):
                            grid[r1][c1]= 2
                            fresh -= 1
                            q.append([r1,c1])
            t += 1


        return t if fresh == 0 else -1
        