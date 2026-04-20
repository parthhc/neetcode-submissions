class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = -1
        while l <= r:
            k = (l + r) // 2
            hours_taken = 0
            for i in range(len(piles)):
                hours_taken += math.ceil(piles[i] / k)

            if hours_taken > h:
                l = k + 1
            else:
                res = k
                r = k - 1


        return res