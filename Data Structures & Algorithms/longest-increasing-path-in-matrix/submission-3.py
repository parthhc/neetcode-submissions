class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        
        visited = set()
        def dfs(i, j):
            if (i, j) in visited: return 0
            if dp[i][j] != 0: return dp[i][j]
            
            visited.add((i, j))
            res = 1
            dxdy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dx, dy in dxdy:
                if i + dx < 0 or i + dx >= len(matrix): continue
                if j + dy < 0 or j + dy >= len(matrix[0]): continue
            
                if matrix[i + dx][j + dy] > matrix[i][j]:
                    res = max(res, 1 + dfs(i + dx, j + dy))
            
            visited.remove((i, j))

            dp[i][j] = res
            return res

        ans = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ans = max(ans, dfs(i, j))

        return ans