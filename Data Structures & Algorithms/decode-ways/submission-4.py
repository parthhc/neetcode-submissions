class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [-1] * len(s)
        dp[0] = 1

        if s[0] == '0': return 0
        
        for i in range(1, len(s)):
            dp[i] = dp[i - 1] if s[i] != 0 else 0

            if s[i] == '0':
                if s[i - 1] in {'1', '2'}:
                    dp[i] = dp[i - 2] if i >= 2 else 1
                else:
                    return 0
            elif s[i - 1] == '1' or (s[i - 1] == '2' and s[i] in '0123456'):
                dp[i] += dp[i - 2] if i >= 2 else 1
        
        return dp[len(s) - 1]