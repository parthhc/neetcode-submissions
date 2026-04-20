class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # get total fresh fruits
        # get coord for rotten fruit
        # bfs through, terminate if there is no where to go

        num_fruits = 0
        q = collections.deque()
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1: num_fruits += 1
                if grid[r][c] == 2: q.append((r, c))

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        time = 0
        
        while q and num_fruits > 0:  
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dirs:
                    newR, newC = r + dr, c + dc
                    if 0 <= newR < len(grid) and 0 <= newC < len(grid[0]) and grid[newR][newC] == 1:
                        num_fruits -= 1
                        grid[newR][newC] = 2
                        q.append((newR, newC))

            time += 1
                
        
        return -1 if num_fruits != 0 else time