class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()
        for n in nums:
            s.add(n)

        res = 0

        for n in s:
            curr_seq = 0
            num = n
            while num in s:
                curr_seq += 1
                num += 1
            
            res = max(curr_seq, res)

        return res