class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float('inf')
        l, total = 0, 0

        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                ans = min(r - l + 1, ans)
                total -= nums[l]
                l += 1

        return 0 if ans == float('inf') else ans