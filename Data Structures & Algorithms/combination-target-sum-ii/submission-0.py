class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()

        def dfs(index, path, summ):
            if summ == target:
                ans.append(path[:])
                return
            if index == len(candidates) or summ > target: return
            
            path.append(candidates[index])
            summ += candidates[index]
            dfs(index + 1, path, summ)
            summ -= candidates[index]
            path.pop()
            
            while index + 1 < len(candidates) and candidates[index] == candidates[index + 1]:
                index += 1
            
            dfs(index + 1, path, summ)


        dfs(0, [], 0)

        return ans