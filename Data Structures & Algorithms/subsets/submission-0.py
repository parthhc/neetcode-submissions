class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        temp = []
        
        def backtrack(i):
            if i == len(nums):
                ans.append(temp[:])
                return

            # skip            
            backtrack(i + 1)

            # pick nums[i]
            temp.append(nums[i])
            backtrack(i + 1)
            temp.pop()

        backtrack(0)
        return ans
