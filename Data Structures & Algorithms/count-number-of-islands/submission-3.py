class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        
        res = 0
        visited = set() # set of tuples, (r, c)

        def dfs(r, c):
            if (r, c) in visited or grid[r][c] == '0': return

            visited.add((r, c))

            if r < len(grid) - 1: dfs(r + 1, c)
            if r > 0: dfs(r - 1, c)
            if c < len(grid[0]) - 1: dfs(r, c + 1)
            if c > 0: dfs(r, c - 1)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r, c) not in visited and grid[r][c] != '0':
                    res += 1
                    dfs(r, c)

        return res

        
                
            