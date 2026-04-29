class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row0 = 0
        

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0 and i != 0:
                    matrix[i][0] = -999
                    matrix[0][j] = -999
                elif matrix[i][j] == 0 and i == 0 :
                    matrix[0][j] = -999
                    row0 = 1
        for i in range(1, len(matrix)):
            if matrix[i][0] == -999:
                for j in range(len(matrix[0])):
                    matrix[i][j] = 0
        for j in range(len(matrix[0])):
            if matrix[0][j] == -999:
                for i in range(len(matrix)):
                    matrix[i][j] = 0
        if row0 == 1:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
        

      