class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        lowest_price = float('inf')

        for p in prices:
            lowest_price = min(lowest_price, p)
            res = max(res, p - lowest_price)

        
        return res