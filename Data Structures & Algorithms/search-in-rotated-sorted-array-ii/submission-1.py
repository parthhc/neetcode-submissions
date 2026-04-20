class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target: return True

            if nums[l] < nums[m]:
                if target < nums[l]:
                    l = m + 1
                elif target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
            elif nums[l] > nums[m]:
                if target > nums[r]:
                    r = m - 1
                elif target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                l += 1
        
        return False