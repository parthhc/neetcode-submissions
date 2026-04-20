class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(houses):
            if not houses: return 0
            if len(houses) == 1: return houses[0]
            
            dp = [-1] * (len(houses) + 1)
            dp[0] = 0
            dp[1] = houses[0]

            for i in range(1, len(houses)):
                dp[i + 1] = max(houses[i] + dp[i - 1], dp[i])

            return dp[len(houses)]

        if len(nums) == 1: return nums[0]
        return max(helper(nums[1:]), helper(nums[:-1]))
            
                