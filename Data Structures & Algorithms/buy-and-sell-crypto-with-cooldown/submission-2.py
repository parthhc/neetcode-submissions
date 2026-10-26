class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        def dfs(i, canBuy):
            if i >= len(prices):
                return 0
            if (i, canBuy) in dp:
                return dp[(i, canBuy)]
            
            res = 0
            if canBuy:
                # case 1: buy
                # case 2: don't
                res = max(res, dfs(i + 1, False) - prices[i])
                res = max(res, dfs(i + 1, True))
            else:
                # case 1: sell
                # case 2: hold
                res = max(res, dfs(i + 2, True) + prices[i])
                res = max(res, dfs(i + 1, False))

            dp[(i, canBuy)] = res
            return res

        return dfs(0, True)

