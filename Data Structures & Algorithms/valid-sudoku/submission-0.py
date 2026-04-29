class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            for j in range(9):
                x = board[i][j]
                if x != ".":
                    for l in range(9):
                        if board[i][l] == x and l!=j:
                            print(i, j, l)
                            print("1")
                            return False
                    for k in range(9):
                        if board[k][j] == x and k != i:
                            print(i, j, k)
                            print("2")
                            return False
                    if i < 3:
                        y = 0
                    elif i < 6:
                        y = 3
                    else:
                        y = 6
                    if j < 3:
                        z = 0
                    elif (j < 6):
                        z = 3
                    else:
                        z = 6
                    for l in range(y, y+3):
                        for k in range(z, z+3):
                            if board[l][k] == x and l!=i and k != j:
                                print(i, j, l, k)
                                print("3")
                                return False
        return True