class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for x in range(len(nums)):
            if (target - nums[x]) in dict.keys(): return [dict.get(target - nums[x]), x]
            dict[nums[x]] = x
        return []