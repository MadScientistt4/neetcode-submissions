class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            checkrow = {}
            checkcol = {}
            sqr = {}
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] not in checkrow:
                        checkrow[board[i][j]] = [i,j]
                    else:
                        return False
                if board[j][i] != ".":
                    if board[j][i] not in checkcol:
                        checkcol[board[j][i]] = [j,i]
                    else:
                        return False
        for square in range(9):
            seen = {}
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen[board[row][col]] = [row, col]
        return True