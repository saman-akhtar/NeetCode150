class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROW, COL = len(board), len(board[0])
      
         
        def dfs(r,c):
          
            board[r][c] = "T"
            dir =[ [0,1],[1,0],[-1,0],[0,-1]]
            for r1,c1 in dir:
                row = r1 + r
                col = c1 + c
                if row  in range(ROW) and col  in range(COL) and board[row][col] == "O":
                    
                    dfs(row,col)
            return

            for r in range(ROW):
                for c in range( COL):
                    if board[r][c]== "O":
                        dfs(r,c)
        #capture border 0 island
        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == "O" and( r in [0,ROW-1] or c in [0,COL-1]):


                    dfs(r,c)

        # make 0 to x
        for r in range(ROW):
                for c in range( COL):
                    if board[r][c]== "O":
                        board[r][c]= 'X'

        # make t to 0
        for r in range(ROW):
                for c in range( COL):
                    if board[r][c]== "T":
                        board[r][c]= 'O'
        