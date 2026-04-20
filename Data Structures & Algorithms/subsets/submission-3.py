class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        stack = []

        def dfs(index):
            if index == len(nums):
                res.append(stack[:])
                return

            stack.append(nums[index])
            index += 1
            dfs(index)
            stack.pop()
            dfs(index)

        dfs(0)
        
        return res