class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        
        res = 0 
        for num in unique:
            seq_len = 1
            temp = num
            if temp + 1 not in unique:
                while temp - 1 in unique:
                    seq_len += 1
                    temp -= 1
            
            res = max(seq_len, res)

        return res