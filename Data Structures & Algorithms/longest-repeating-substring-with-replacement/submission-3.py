class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letter_freq = {}
        l = 0
        max_freq = 0

        res = 0

        for r in range(len(s)):
            letter_freq[s[r]] = letter_freq.get(s[r], 0) + 1

            for key, value in letter_freq.items():
                if value > max_freq:
                    max_freq = value
            
            while max_freq + k < r - l + 1:
                letter_freq[s[l]] -= 1
                for key, value in letter_freq.items():
                    if value > max_freq:
                        max_freq = value
                l += 1
            
            res = max(res, r - l + 1)


        return res