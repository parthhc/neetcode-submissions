class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        visited = set()

        dp = {} # (r, c) : path len

        def dfs(r, c):
            if (r, c) in dp:
                return dp[(r, c)]

            res = 1
            if r + 1 < len(matrix) and matrix[r][c] < matrix[r + 1][c]:
                res = max(res, dfs(r + 1, c) + 1)
            if r - 1 >= 0 and matrix[r][c] < matrix[r - 1][c]:
                res = max(res, dfs(r - 1, c) + 1)
            if c + 1 < len(matrix[0]) and matrix[r][c] < matrix[r][c + 1]:
                res = max(res, dfs(r, c + 1) + 1)
            if c - 1 >= 0 and matrix[r][c] < matrix[r][c - 1]:
                res = max(res, dfs(r, c - 1) + 1)

            dp[(r, c)] = res
            return res

        res = 1
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                res = max(res, dfs(r, c))

        return res
            
