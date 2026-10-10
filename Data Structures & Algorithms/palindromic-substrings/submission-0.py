class Solution:
    def countSubstrings(self, s: str) -> int:
        # 2 cases: even len, odd len
        res = 0

        for i in range(len(s)):
            res += 1

            # odd len
            l = i - 1
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            
            # even len
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

        return res