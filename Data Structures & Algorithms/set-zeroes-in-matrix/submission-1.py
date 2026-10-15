class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        setFirstRow = False
        setFirstCol = False

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == 0 and j == 0 and matrix[i][j] == 0:
                    setFirstRow = True
                    setFirstCol = True
                elif i == 0 and matrix[i][j] == 0:
                    setFirstRow = True
                elif j == 0 and matrix[i][j] == 0:
                    setFirstCol = True
                elif matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                for j in range(len(matrix[0])):
                    matrix[i][j] = 0

        for j in range(1, len(matrix[0])):
            if matrix[0][j] == 0:
                for i in range(len(matrix)):
                    matrix[i][j] = 0

        if setFirstRow:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0

        if setFirstCol:
            for i in range(len(matrix)):
                matrix[i][0] = 0
        