class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        dp = [[-1] * (amount + 1) for i in range(len(coins) + 1)]

        def memoHelper(i, a):
            if a == 0: return 1
            if a < 0 or i >= len(coins): return 0  

            if dp[i][a] == -1:
                res = 0
                if coins[i] <= a:
                    res = memoHelper(i + 1, a) + memoHelper(i, a - coins[i])

                dp[i][a] = res

            return dp[i][a]

        return memoHelper(0, amount)