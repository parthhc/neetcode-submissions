class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False
        s1 = Counter(s)
        s2 = Counter(t)

        for key, value in s1.items():
            if key not in s2: return False
            if s2[key] != s1[key]: return False

        if len(s1) != len(s2): return False

        return True        
