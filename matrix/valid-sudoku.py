class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        box = [(0,0),(0,1),(0,2),
               (1,0),(1,1),(1,2),
               (2,0),(2,1),(2,2)]
        
        for i in range(9):
            row, col = set(), set()
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in row: 
                        return False
                    row.add(board[i][j])
                if board[j][i] != '.':
                    if board[j][i] in col: 
                        return False
                    col.add(board[j][i])
        
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                seen = set()
                for dr, dc in box:
                    if board[i+dr][j+dc] != '.':
                        if board[i+dr][j+dc] in seen: 
                            return False
                        seen.add(board[i+dr][j+dc])
        
        return True