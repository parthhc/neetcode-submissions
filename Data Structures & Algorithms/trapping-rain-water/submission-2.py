class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = [0] * len(height)
        right_max = [0] * len(height)

        for i in range(len(height)):
            h = height[i]
            if i == 0:
                left_max[i] = h
            else:
                left_max[i] = max(left_max[i - 1], h)
        
        for i in range(len(height) - 1, -1, -1):
            h = height[i]
            if i == len(height) - 1:
                right_max[i] = h
            else:
                right_max[i] = max(right_max[i + 1], h)

        res = 0

        for i in range(len(height)):
            h = height[i]
            l_max = left_max[i]
            r_max = right_max[i]

            res += min(r_max, l_max) - h

        return res