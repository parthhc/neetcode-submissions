class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if word == "": return True
        if not board: return False
        if not board[0]: return False

        def dfs(r, c, i, visited):
            if i == len(word): return True
            if r < 0 or r >= len(board): return False
            if c < 0 or c >= len(board[0]): return False
            if (r, c) in visited: return False
            if board[r][c] != word[i]: return False

            visited.add((r, c))
            found = (dfs(r + 1, c, i + 1, visited) or
                dfs(r - 1, c, i + 1, visited) or
                dfs(r, c + 1, i + 1, visited) or
                dfs(r, c - 1, i + 1, visited))
            visited.remove((r, c))
            return found

        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r, c, 0, set()):
                    return True

        return False