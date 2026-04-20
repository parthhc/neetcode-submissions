class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        res = 0

        def dfs(row, col):
            if (row, col) in visited or grid[row][col] == "0": return
            visited.add((row, col))

            if row + 1 < len(grid):
                dfs(row + 1, col)

            if row - 1 >= 0:
                dfs(row - 1, col)
            
            if col + 1 < len(grid[0]):
                dfs(row, col + 1)
            
            if col - 1 >= 0:
                dfs(row, col - 1)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row, col) in visited or grid[row][col] == "0":
                    continue
                else:
                    dfs(row, col)
                    res += 1

        return res
