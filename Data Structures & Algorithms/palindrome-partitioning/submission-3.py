class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def isPalindrome(l, r):
            while l < r:
                if s[r] != s[l]: return False
                l += 1
                r -= 1

            return True

        res = []

        stack = []

        def backtrack(l):
            if l >= len(s):
                res.append(stack[:])
                return
            
            for r in range(l, len(s)):
                if isPalindrome(l, r):
                    stack.append(s[l : r+1])
                    backtrack(r + 1)
                    stack.pop()

        backtrack(0)
        return res

                    

            