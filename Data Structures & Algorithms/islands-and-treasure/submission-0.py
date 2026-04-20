class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = collections.deque()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0: q.append((0, (r, c)))
                # storing tuples with dist from chest and coords

        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        while q:
            for _ in range(len(q)):
                dist, coord = q.popleft()
                r, c = coord
                for dr, dc in dirs:
                    newR, newC = r + dr, c + dc
                    if 0 <= newR < len(grid) and 0 <= newC < len(grid[0]) and grid[newR][newC] != -1:
                        if dist + 1 < grid[newR][newC]:
                            grid[newR][newC] = dist + 1
                            q.append((grid[newR][newC], (newR, newC)))

                

        