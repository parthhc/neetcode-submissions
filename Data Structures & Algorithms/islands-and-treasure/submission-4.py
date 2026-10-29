class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        inf = 2**31 - 1

        q = collections.deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i, j))

        dxdy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            i, j = q.popleft()
            for dx, dy in dxdy:
                x, y = i + dx, j + dy
                if x < 0 or x >= len(grid): continue
                if y < 0 or y >= len(grid[0]): continue
                if grid[x][y] != inf: continue

                grid[x][y] = 1 + grid[i][j]
                q.append((x, y))
