class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(i, r, c):
            if i == len(word): return True
            if (r, c) in visited: return False
            if not (0 <= r < len(board)): return False
            if not (0 <= c < len(board[0])): return False
            if word[i] != board[r][c]: return False

            i += 1
            res = False
            visited.add((r, c))
            for dr, dc in dirs:
                res = dfs(i, r + dr, c + dc) or res

            visited.remove((r, c))

            return res

        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(0, r, c): return True

        return False