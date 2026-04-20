class Solution:
    def canJump(self, nums: List[int]) -> bool:
        pos_to_reach = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= pos_to_reach:
                pos_to_reach = i

        return pos_to_reach == 0