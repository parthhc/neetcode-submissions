class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_min = 1
        curr_max = 1
        res = float('-inf')

        for n in nums:
            new_min = min(curr_min * n, curr_max * n, n)
            new_max = max(curr_min * n, curr_max * n, n)

            curr_min, curr_max = new_min, new_max

            res = max(res, curr_max)

        
        return res