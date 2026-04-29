class Solution:
    def solve(self, board: List[List[str]]) -> None:
        edges = set()
        row, col = len(board), len(board[0])
        def dfs(i, j, visit):
            if (i < 0 or i >= row) or (j < 0 or j >= col) or (i, j) in visit or board[i][j] == "X":
                return
            visit.add((i, j))
            direc = [[0, 1], [1, 0], [0, -1], [-1, 0]]
            for dx, dy in direc:
                nx, ny = i + dx, j + dy
                if (0 <= nx < row and 0 <= ny < col) and board[nx][ny] == "O":
                    dfs(nx, ny, visit)

        for i in range(row):
            dfs(i, 0, edges)
            dfs(i, col-1, edges)

        for j in range(col):
            dfs(0, j, edges)
            dfs(row-1, j, edges)
        print(edges)

        for i in range(row):
            for j in range(col):
                if board[i][j] == "O" and (i, j) not in edges:
                    board[i][j] = "X"