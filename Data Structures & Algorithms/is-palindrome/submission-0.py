class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum())
        s1 = list(s)
        l, r = 0, len(s) - 1
        while l < r:
            if s1[l].lower() != s1[r].lower(): return False
            l += 1
            r -= 1
        return True