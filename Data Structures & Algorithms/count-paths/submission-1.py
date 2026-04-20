class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for i in range(n)] for j in range(m)]

        def memoHelper(i, j):
            if i == m - 1 or j == n - 1: return 1
            if i >= m or j >= n: return 0
            if dp[i][j] == -1:
                dp[i][j] = memoHelper(i + 1, j) + memoHelper(i, j + 1)
            
            return dp[i][j]


        return memoHelper(0, 0)
