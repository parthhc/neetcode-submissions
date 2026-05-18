class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        h, w = len(matrix), len(matrix[0])
        l, r = 0, h*w - 1

        while l <= r:
            m = (l + r) // 2

            row = m // w
            col = m % w

            if matrix[row][col] == target: 
                return True
            elif matrix[row][col] < target:
                l = m + 1
            else:
                r = m - 1

        return False

