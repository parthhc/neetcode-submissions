class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1

        max_area = -1;

        while l <= r:
            left_h = heights[l]
            right_h = heights[r]

            area = min(left_h, right_h)*(r - l)
            max_area = max(area, max_area)

            if left_h < right_h:
                l += 1
            else:
                r -= 1
        
        return max_area
        
