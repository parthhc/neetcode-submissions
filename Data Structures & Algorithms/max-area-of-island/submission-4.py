class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        ans = 0
        visited = set()

        def dfs(r, c):
            if r >= len(grid) or r < 0: return 0
            if c >= len(grid[0]) or c < 0: return 0
            if (r, c) in visited or grid[r][c] == 0: return 0

            visited.add((r, c))

            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)


        for r in range(len(grid)):
            for c in range(len(grid[0])):
                ans = max(dfs(r, c), ans)

        return ans

