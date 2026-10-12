class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_pal_len = 1
        res = s[0]

        for i in range(1, len(s)):
            pal_len = 0

            # odd case
            l, r = i - 1, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if max_pal_len < r - l:
                max_pal_len = r - l
                res = s[l+1:r]

            # even case
            l, r = i - 1, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if max_pal_len < r - l:
                max_pal_len = r - l
                res = s[l+1:r]


        return res