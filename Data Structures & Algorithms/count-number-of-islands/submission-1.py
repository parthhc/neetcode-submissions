class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0

        visited = set()
        ans = 0

        def dfs(r, c):
            if r not in range(len(grid)): return
            if c not in range(len(grid[0])): return
            if (r, c) in visited: return
            visited.add((r, c))
            if grid[r][c] == '0': return
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)



        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '0' or (r, c) in visited:
                    continue
                ans += 1
                dfs(r, c)
        
        return ans

        
                
            