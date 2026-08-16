class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        res = 0

        for n in nums:
            if n - 1 not in seen:
                seq = 1
                while n + seq in seen:
                    seq += 1
                
                res = max(seq, res)

        return res