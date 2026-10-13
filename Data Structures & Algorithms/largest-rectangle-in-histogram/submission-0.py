class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0

        for i in range(len(heights)):
            furthest_backwards_extension = i
            while stack and stack[-1][0] > heights[i]:
                height, pos = stack.pop()
                best_area = height * (i - pos)
                res = max(res, best_area)
                furthest_backwards_extension = pos

            stack.append((heights[i], furthest_backwards_extension))

        while stack:
            height, pos = stack.pop()
            best_area = height * (len(heights) - pos)
            res = max(res, best_area)

        return res