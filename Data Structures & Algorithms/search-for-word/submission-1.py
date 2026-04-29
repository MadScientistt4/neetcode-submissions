class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.isExist = False
        def function(i, j, k, visited):
            if k == len(word):
                return True
            if i >= len(board) or j >= len(board[0]) or i<0 or j<0:
                return False
            
            if board[i][j] == word[k] and (i,j) not in visited:
                print(board[i][j], i, j)
                visited.add((i, j))
                res = (function(i, j+1, k+1, visited) 
                or function(i, j-1, k+1, visited)
                or function(i+1, j, k+1, visited) 
                or function(i-1, j, k+1, visited) 
                )
                visited.remove((i,j))
                return res
            else:
                return False
        for i in range(len(board)):
            for j in range(len(board[i])):
                if function(i, j, 0, set()):
                    return True
        return False
