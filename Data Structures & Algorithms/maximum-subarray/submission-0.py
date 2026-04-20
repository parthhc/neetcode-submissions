class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float('-inf')
        curr_sum = float('-inf')

        for n in nums:
            if n > curr_sum + n:
                curr_sum = n
            else:
                curr_sum += n
            
            res = max(res, curr_sum)

        return res