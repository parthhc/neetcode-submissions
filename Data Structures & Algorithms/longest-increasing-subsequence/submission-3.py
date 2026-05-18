class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)

        def memo(i):
            if dp[i] != -1: return dp[i]

            dp[i] = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], 1 + memo(j))

            return dp[i]

        for k in range(len(nums)):
            memo(k)

        return max(dp)