class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0

        for i, h in enumerate(heights):
            furthest_height_extention = i
            while stack and stack[-1][0] > h:
                height, pos = stack.pop()
                res = max(res, (i - pos) * height)
                furthest_height_extention = pos
            
            stack.append((h, furthest_height_extention))

        while stack:
            height, pos = stack.pop()
            res = max(res, (len(heights) - pos) * height)

        return res