class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()
        for n in nums:
            s.add(n)

        soln = 0

        for num in s:
            curr_seq = 0
            n = num
            while n in s:
                curr_seq += 1
                n += 1

            soln = max(curr_seq, soln)

        return soln