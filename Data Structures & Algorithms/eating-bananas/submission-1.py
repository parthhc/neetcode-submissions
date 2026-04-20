class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        k = r
        while l <= r:
            m = (l + r) // 2

            hours_taken = 0

            for i in range(len(piles)):
                hours_taken += math.ceil(piles[i] / m)

            if hours_taken <= h:
                k = min(k, m)
                r = m - 1
            else:
                l = m + 1

        
        return k