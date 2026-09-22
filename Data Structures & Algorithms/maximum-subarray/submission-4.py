class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        curr_sum = res

        for i in range(1, len(nums)):
            num = nums[i]
            if num + curr_sum < num:
                curr_sum = num
            else:
                curr_sum += num
            
            res = max(curr_sum, res)

        return res