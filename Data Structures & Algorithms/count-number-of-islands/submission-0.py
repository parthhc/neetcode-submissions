class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0

        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        ans = 0

        def bfs(r, c):
            q = collections.deque()
            visited[r][c] = True
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
                for dr, dc in directions:
                    next_pos_row, next_pos_col = row + dr, col + dc
                    if next_pos_row in range(len(grid)) and next_pos_col in range(len(grid[0])) and grid[next_pos_row][next_pos_col] == "1" and not visited[next_pos_row][next_pos_col]:
                        visited[next_pos_row][next_pos_col] = True
                        q.append((next_pos_row, next_pos_col))

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "0" or visited[r][c]:
                    continue
                bfs(r, c)
                ans += 1

        return ans
                
            