class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        COL = len(board[0])
        ROW = len(board)
        rowSet = defaultdict(set)
        colSet = defaultdict(set)
        boxSet = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] != "." and (board[i][j]  in rowSet[i] or board[i][j]  in colSet[j] or board[i][j]  in boxSet[(i//3,j//3)]):
                
                    return False
                rowSet[i].add(board[i][j])
                colSet[j].add(board[i][j])
                boxSet[(i//3,j//3)].add(board[i][j])
        return True




# TC O(9^2)
# SC O(9^2)





        
        COL = len(board[0])
        ROW = len(board)
        rowSet = defaultdict(set)
        colSet = defaultdict(set)
        boxSet = defaultdict(set)


        for r in range(ROW):
            for c in range(COL):
                if (board[r][c] != ".") and (board[r][c] in rowSet[r] or board[r][c] in colSet[c] or board[r][c] in boxSet[(r//3,c//3)]):
                    return False
                rowSet[r].add(board[r][c])
                colSet[c].add(board[r][c])
                boxSet[(r//3,c//3)].add(board[r][c])
        return True

# TC O(9^2)
# SC O(9^2)
        