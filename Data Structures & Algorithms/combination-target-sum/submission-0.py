class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        stack = []
        soln = []

        def backtrack(i, sum_so_far):
            if sum_so_far == target and stack not in soln:
                soln.append(stack[:])
            if i == len(nums) or sum_so_far > target:
                return

            backtrack(i+1, sum_so_far) # skip current number

            stack.append(nums[i])
            backtrack(i, sum_so_far + nums[i])
            stack.pop()

        backtrack(0, 0)

        return soln