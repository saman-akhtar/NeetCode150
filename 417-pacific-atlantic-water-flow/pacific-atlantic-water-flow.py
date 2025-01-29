class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac = set()
        atl = set()

        def dfs(r, c, visit, prevH):
            if ((r, c) in visit or r not in range(ROWS) or c not in range(COLS)  or heights[r][c] < prevH):
                return
            
            visit.add((r, c))  # **Fix: Mark as visited before exploring further**
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for dr, dc in directions:
                dfs(r + dr, c + dc, visit, heights[r][c])  # **Fix: Pass current height**

        # **Start DFS from Pacific and Atlantic edges**
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])          # **Left border (Pacific)**
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])  # **Right border (Atlantic)**

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])          # **Top border (Pacific)**
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])  # **Bottom border (Atlantic)**

        # **Find all cells that can reach both oceans**
        return list(pac & atl)

        # TC O(m×n)
        # SC O(m×n)

        # BRIUET force on eac cell = O(m ^ 2×n ^ 2)