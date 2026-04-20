class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letter_freq = {}

        l = 0
        res = 0

        for r in range(len(s)):
            letter_freq[s[r]] = letter_freq.get(s[r], 0) + 1

            max_freq = 0

            for key, value in letter_freq.items():
                max_freq = max(value, max_freq)

            while (r - l + 1) - max_freq > k:
                letter_freq[s[l]] -= 1
                l += 1
                for key, value in letter_freq.items():
                    max_freq = max(value, max_freq)

            res = max(res, r - l + 1)

        return res
