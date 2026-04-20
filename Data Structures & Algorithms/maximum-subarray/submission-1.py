class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = sum_so_far = float('-inf')

        for i in range(len(nums)):
            if nums[i] > sum_so_far + nums[i]:
                sum_so_far = 0
            
            sum_so_far += nums[i]
            res = max(sum_so_far, res)

        return res