class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for x in range(len(nums)):
            if nums[x] in seen: return True
            seen.add(nums[x])
        return False;
         