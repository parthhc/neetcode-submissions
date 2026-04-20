class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        ans = 0
        visited = set()

        def bfs(r, c):
            queue = collections.deque()
            queue.append((r, c))
            visited.add((r, c))
            area = 1

            while queue:
                directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
                row, col = queue.popleft()
                for dr, dc in directions:
                    new_row = row + dr
                    new_col = col + dc
                    if new_row in range(len(grid)) and new_col in range(len(grid[0])) and (new_row, new_col) not in visited and grid[new_row][new_col] == 1:
                        queue.append((new_row, new_col))
                        visited.add((new_row, new_col))
                        area += 1

            return area

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row, col) in visited or grid[row][col] == 0:
                    continue
                ans = max(ans, bfs(row, col))
        
        return ans
