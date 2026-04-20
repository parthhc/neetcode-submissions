class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()

        def dfs(r, c, ocean, prevHeight):
            if ((r, c) in ocean or 
            r < 0 or c < 0 or 
            r > len(heights) - 1 or c > len(heights[0]) - 1 
            or heights[r][c] < prevHeight):
                return
            
            ocean.add((r, c))
            dfs(r + 1, c, ocean, heights[r][c])
            dfs(r - 1, c, ocean, heights[r][c])
            dfs(r, c - 1, ocean, heights[r][c])
            dfs(r, c + 1, ocean, heights[r][c])

        for r in range(len(heights)):
            if (r, 0) not in pacific:
                dfs(r, 0, pacific, 0)
            
            if (r, len(heights[0]) - 1) not in atlantic:
                dfs(r, len(heights[0]) - 1, atlantic, 0)
                
        for c in range(len(heights[0])):
            if (0, c) not in pacific:
                dfs(0, c, pacific, 0)
            
            if (len(heights) - 1, c) not in atlantic:
                dfs(len(heights) - 1, c, atlantic, 0)

        res = []
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])

        return res
