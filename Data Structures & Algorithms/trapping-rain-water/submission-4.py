class Solution:
    def trap(self, height: List[int]) -> int:
        l_max, r_max = height[0], height[-1]

        l, r = 1, len(height) - 2
        res = 0

        while l <= r:
            if l_max <= r_max:
                res += max(0, l_max - height[l])
                l_max = max(l_max, height[l])
                l += 1
            else:
                res += max(0, r_max - height[r])
                r_max = max(r_max, height[r])
                r -= 1

        return res