class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res, curr_sum = nums[0], nums[0]

        for n in nums[1:]:
            if curr_sum + n < n:
                curr_sum = n
            else:
                curr_sum += n
            
            res = max(res, curr_sum)

        return res