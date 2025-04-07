class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        ROW,COL = len(grid), len(grid[0])
        visit = set()
        max_area = 0
        dir = [[1,0],[0,1],[0,-1],[-1,0]]
        def bfs(r,c):
            # nonlocal dir
            visit.add((r,c))
            q = deque([(r,c)])
            cur_area = 1
            while q:
                r1,c1 = q.popleft()
                # No Level Distinction Needed so no nned to popleft in loop
                for dr,dc in dir:
                    row,col = dr + r1, dc + c1
                    if (row,col) not in visit and row in range(ROW ) and col in range(COL) and grid[row][col] == 1:
                        q.append((row,col))
                        # in dfs u dont add in visit bit here add
                        visit.add((row,col))
                        cur_area += 1
            return cur_area



        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1 and (r,c) not in visit:
                    area = bfs(r,c)
                    max_area = max(area, max_area)
        return max_area

# TC O(N.M)

# SC 