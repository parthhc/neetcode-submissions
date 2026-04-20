class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = list(s)
        s2 = list(t)
        if len(s1) != len(s2): 
            return False
        s1.sort()
        s2.sort()
        for x in range(len(s1)):
            if s1[x] != s2[x]:
                return False
        return True
