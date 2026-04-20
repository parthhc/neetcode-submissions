class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {}

        def memoNumDecodings(i):
            if i == len(s): return 1
            if s[i] == "0": return 0
            if i not in dp:
                res = memoNumDecodings(i + 1)

                if i + 1 < len(s) and (
                    (s[i] == '1' and s[i + 1] in '0123456789')
                    or 
                    (s[i] == '2' and s[i + 1] in '0123456')
                ):
                    res += memoNumDecodings(i + 2)
                
                dp[i] = res
            
            return dp[i]
        
        return memoNumDecodings(0)