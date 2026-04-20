class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        num_fruit = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    num_fruit += 1

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        time = 0
        while q:
            num_rotten_fruit = len(q)

            for i in range(num_rotten_fruit):
                r, c = q.popleft()

                for dr, dc in dirs:
                    new_r, new_c = r + dr, c + dc

                    if 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]) and grid[new_r][new_c] == 1:
                        grid[new_r][new_c] = 2
                        num_fruit -= 1
                        q.append((new_r, new_c))

            if q: time += 1

        return time if num_fruit == 0 else -1