class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        first_window = nums[:k]
        res.append(max(first_window))

        l = 1

        for r in range(k, len(nums)):
            window = nums[l:r+1]
            res.append(max(window))

            l += 1

        return res
        