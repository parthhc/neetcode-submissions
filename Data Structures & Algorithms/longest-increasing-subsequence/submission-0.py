class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)

        def memoHelper(i):
            if dp[i] == 0:
                dp[i] = 1
                for j in range(i):
                    if nums[i] > nums[j]:
                        dp[i] = max(dp[i], 1 + memoHelper(j))
            
            return dp[i]

        res = 0
        for i in range(len(nums)):
            res = max(res, memoHelper(i))

        return res

        