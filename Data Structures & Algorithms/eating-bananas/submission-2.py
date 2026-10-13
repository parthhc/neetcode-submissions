class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        res = max(piles)
       
        while l <= r:
            m = (l + r) // 2

            hours_spent = 0
            for pile in piles:
                hours_spent += math.ceil(pile / m)
            
            if hours_spent > h:
                l = m + 1
            else:
                res = m
                r = m - 1

        
        return res