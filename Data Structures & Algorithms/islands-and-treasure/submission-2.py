class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = collections.deque()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0: q.append((r, c))

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                newR, newC = r + dr, c + dc
                if 0 <= newR < len(grid) and 0 <= newC < len(grid[0]) and grid[newR][newC] == (2 ** 31) - 1:
                    grid[newR][newC] = grid[r][c] + 1
                    q.append((newR, newC))