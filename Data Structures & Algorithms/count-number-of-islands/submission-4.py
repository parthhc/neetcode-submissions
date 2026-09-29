class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        res = 0

        def dfs(r, c):
            if (r, c) in visited: return
            if r < 0 or r >= len(grid): return
            if c < 0 or c >= len(grid[0]): return
            if grid[r][c] == '0': return

            visited.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r, c) not in visited and grid[r][c] == '1':
                    dfs(r, c)
                    res += 1
        
        return res
