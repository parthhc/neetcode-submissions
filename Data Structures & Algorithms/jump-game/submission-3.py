class Solution:
    def canJump(self, nums: List[int]) -> bool:
        pos_to_reach = len(nums) - 1
        
        for i in range(len(nums) - 2, -1, -1):
            jump_dist = nums[i]

            if i + jump_dist >= pos_to_reach:
                pos_to_reach = i

        return True if pos_to_reach == 0 else False