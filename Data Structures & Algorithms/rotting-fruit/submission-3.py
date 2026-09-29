class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        num_fruit = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    num_fruit += 1
                elif grid[r][c] == 2:
                    q.append((r, c))

        res = 0
        dxdy = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while q:
            if num_fruit == 0: break
            
            level_len = len(q)
            for i in range(level_len):
                r, c = q.popleft()

                for dx, dy in dxdy:
                    new_r, new_c = r + dx, c + dy

                    if new_r < 0 or new_r >= len(grid): continue
                    if new_c < 0 or new_c >= len(grid[0]): continue
                    if grid[new_r][new_c] == 2 or grid[new_r][new_c] == 0:
                        continue
                    
                    grid[new_r][new_c] = 2
                    num_fruit -= 1
                    q.append((new_r, new_c))
            
            res += 1
        
        return res if num_fruit == 0 else -1