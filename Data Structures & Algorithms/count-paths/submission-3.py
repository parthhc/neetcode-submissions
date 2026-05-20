class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1] * n for _ in range(m)]
        dp[0][0] = 1

        def memo(x, y):
            if not (0 <= x < m): return 0
            if not (0 <= y < n): return 0
            if dp[x][y] != -1: return dp[x][y]

            dp[x][y] = memo(x - 1, y) + memo(x, y - 1)

            return dp[x][y]


        return memo(m - 1, n - 1)