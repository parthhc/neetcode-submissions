class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False

        target = sum(nums) // 2

        dp = {}
        def dfs(i, curr_sum):
            if curr_sum == target:
                return True
            if i == len(nums):
                return False
            if (i, curr_sum) in dp:
                return dp[(i, curr_sum)]

            res = dfs(i + 1, curr_sum + nums[i]) or dfs(i + 1, curr_sum)

            dp[(i, curr_sum)] = res
            return res

        return dfs(0, 0)

            