class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort() # sort list for 2 pointer

        for i in range(len(nums)):
            if nums[i] > 0: break # greater than 0, sum needs to equal 0
            if i > 0 and nums[i] == nums[i - 1]: continue # avoid duplicates

            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and r != len(nums) - 1 and nums[r] == nums[r + 1]:
                        r -= 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
            
        return ans