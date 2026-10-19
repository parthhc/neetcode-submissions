class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {} # (i, canBuy) : profit
        
        def dfs(i, canBuy):
            if i >= len(prices):
                return 0
            
            if (i, canBuy) in dp:
                return dp[(i, canBuy)]

            res = 0
            if canBuy:
                res = max(
                    dfs(i + 1, False) - prices[i], 
                    dfs(i + 1, True)
                )
            else:
                res = max(
                    dfs(i + 2, True) + prices[i],
                    dfs(i + 1, False)
                )

            dp[(i, canBuy)] = res
            return res

        return dfs(0, True)