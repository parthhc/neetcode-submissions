class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s not in res:
                res[sorted_s] = [s]
            else:
                res[sorted_s].append(s)

        return list(res.values())