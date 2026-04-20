class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0

        for i in range(len(nums)):
            if nums[i] - 1 not in s:
                length = 1
                while nums[i] + length in s:
                    length += 1
                res = max(res, length)    

        return res