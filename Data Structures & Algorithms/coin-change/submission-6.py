class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount + 1)
        dp[0] = 0

        def memo(am):
            if dp[am] != -1: return dp[am]

            best = 1e9
            for c in coins:
                if am - c >= 0:
                    best = min(best, 1 + memo(am - c))

            dp[am] = best
            return dp[am]

        res = memo(amount)
        return res if res != 1e9 else -1
