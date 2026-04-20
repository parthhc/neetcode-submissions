class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        l, r = 0, len(heights) - 1

        while l < r:
            left_height = heights[l]
            right_height = heights[r]

            area = min(left_height, right_height) * (r - l)

            ans = max(ans, area)

            if left_height < right_height:
                l += 1
            else:
                r -= 1
        
        return ans