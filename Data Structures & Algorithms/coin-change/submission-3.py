class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount + 1)
        dp[0] = 0

        def memo(i):
            if i == 0: return 0
            if dp[i] != -1: return dp[i]

            dp[i] = float('inf')
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], memo(i - c) + 1)

            return dp[i]
        
        res = memo(amount)
        return res if res != float('inf') else -1