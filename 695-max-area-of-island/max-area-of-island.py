class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0
        row,col = len(grid), len(grid[0])
        visit = set()

        def bfs(r,c):
            visit.add((r,c))
            q = deque([])
            q.append((r,c))
            area =  1
            while q:
                for i in range(len(q)):
                    rq,cq = q.popleft()
                    dirs = [[1,0],[-1,0],[0,1],[0,-1]]

                    for (dr,dc) in dirs:
                        r1 = dr + rq
                        c1 = dc + cq
                        if((r1,c1) not in visit and r1 in range(row) and c1 in range(col) and grid[r1][c1] ==1 ):
                            visit.add((r1,c1)) 
                            q.append((r1,c1))
                            area += 1
            return area
        
        for r in range(row):
            for c in range(col):
                if(grid[r][c]== 1 and (r,c) not in visit):
                    cur_area = bfs(r,c)
                    area = max(area, cur_area)
        return area
        