class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        starting_points = collections.deque()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    starting_points.append((r, c))

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while starting_points:
            r, c = starting_points.popleft()

            for dr, dc in dirs:
                new_r, new_c = r + dr, c + dc

                if 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]) and grid[new_r][new_c] == 2147483647:
                    grid[new_r][new_c] = grid[r][c] + 1
                    starting_points.append((new_r, new_c))