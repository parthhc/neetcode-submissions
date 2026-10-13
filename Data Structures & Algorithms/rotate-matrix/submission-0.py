class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # transpose
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for mtx in matrix:
            mtx.reverse()