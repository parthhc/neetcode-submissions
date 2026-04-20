class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[-1 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

        for i in range(len(text1) + 1):
            dp[i][0] = 0

        for j in range(len(text2) + 1):
            dp[0][j] = 0

        def memoHelper(i, j):
            if i < 0 or j < 0: return 0
            if dp[i][j] == -1:
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + memoHelper(i - 1, j - 1)
                else:
                    dp[i][j] = max(memoHelper(i - 1, j), memoHelper(i, j - 1))

            return dp[i][j]


        return memoHelper(len(text1), len(text2))