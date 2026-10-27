class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(len(s)):
            for word in wordDict:
                start = i - len(word) + 1
                if start >= 0 and dp[start] and word == s[start:i + 1]:
                    dp[i + 1] = True
                    break

        return dp[-1]