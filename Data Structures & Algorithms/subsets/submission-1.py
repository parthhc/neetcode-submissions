class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        stack = []
        soln = []

        def backtrack(i):
            if i == len(nums):
                soln.append(stack[:])
                return

            backtrack(i + 1)

            stack.append(nums[i])
            backtrack(i + 1)
            stack.pop()

        backtrack(0)

        return soln
