# Rat in a Maze
# Difficulty: MediumAccuracy: 35.75%Submissions: 410K+Points: 4Average Time: 25m
# Consider a rat placed at position (0, 0) in an n x n square matrix maze[][]. The rat's goal is to reach the destination at position (n-1, n-1). The rat can move in four possible directions: 'U'(up), 'D'(down), 'L' (left), 'R' (right).

# The matrix contains only two possible values:

# 0: A blocked cell through which the rat cannot travel.
# 1: A free cell that the rat can pass through.
# Your task is to find all possible paths the rat can take to reach the destination, starting from (0, 0) and ending at (n-1, n-1), under the condition that the rat cannot revisit any cell along the same path. Furthermore, the rat can only move to adjacent cells that are within the bounds of the matrix and not blocked.
# If no path exists, return an empty list.

# Note: Return the final result vector in lexicographically smallest order.

# Examples:

# Input: maze[][] = [[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]
# Output: ["DDRDRR", "DRDDRR"]
# Explanation: The rat can reach the destination at (3, 3) from (0, 0) by two paths - DRDDRR and DDRDRR, when printed in sorted order we get DDRDRR DRDDRR.

class Solution:
    def ratInMaze(self, maze):
        # code here
        if maze[0][0] == 0: return []
        row = len(maze)
        col = len(maze[0])
        path = []
        visited = set()
        directions = [(1, 0, "D"), (0, -1, "L"), (0, 1, "R"), (-1, 0, "U")]
        def solve(i,j,cur_path):
            if i == row - 1 and j ==  col-1:
                path.append(cur_path)
                return
            visited.add((i,j))
            for di, dj,char in directions:
                cur_i= di + i
                cur_j = dj + j
                if 0 <= cur_i < row and 0 <= cur_j < col  and (cur_i,cur_j) not in visited and maze[cur_i][cur_j] ==1:
                    solve(cur_i,cur_j, cur_path + char)
                   
            # 2. BACKTRACK: Unmark this cell so other paths can use it
            visited.remove((i, j))
        solve(0,0,"")    
        return path
        
        # Comparison: DFS vs. BacktrackingFeatureStandard DFS (No Unmarking)Backtracking (With Unmarking)Logic"Find any path. Once a cell is visited, it's done.""Find all paths. Use a cell, then free it for other paths."Time Complexity$O(V + E) \rightarrow O(N^2)$$O(4^{N^2})$Space Complexity$O(N^2)$$O(N^2)$
