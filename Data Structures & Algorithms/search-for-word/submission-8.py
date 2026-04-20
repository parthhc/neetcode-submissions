class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word: return True
        if not board: return False
        if not board[0]: return False

        visited = set()

        def dfs(r, c, idx):
            if idx == len(word): return True
            if (r, c) in visited: return False
            if r < 0 or r >= len(board): return False
            if c < 0 or c >= len(board[0]): return False

            if board[r][c] != word[idx]: return False

            visited.add((r, c))
            idx += 1

            res = dfs(r + 1, c, idx) or dfs(r - 1, c, idx) or dfs(r, c + 1, idx) or dfs(r, c - 1, idx)
            
            visited.remove((r, c))

            return res


        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r, c, 0): return True
        

        return False