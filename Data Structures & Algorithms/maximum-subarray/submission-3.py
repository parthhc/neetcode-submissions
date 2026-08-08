class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float('-inf')
        summ = res
        for n in nums:
            if n > summ + n:
                summ = n
            else:
                summ += n
            
            res = max(summ, res)

        return res