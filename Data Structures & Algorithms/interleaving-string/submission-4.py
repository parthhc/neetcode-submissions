class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3): return False
        
        dp = {} # (i, j): bool
        
        def dfs(i, j, word):
            if word == s3:
                return True
            if (i, j) in dp: 
                return dp[(i, j)]

            res = False
            k = i + j

            if i < len(s1) and s3[k] == s1[i]:
                res = dfs(i + 1, j, word + s1[i])
                    
            
            if not res and j < len(s2) and s3[k] == s2[j]:
                res = dfs(i, j + 1, word + s2[j])
            
            dp[(i, j)]= res
            return res

        return dfs(0, 0, "")
