class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if word == "": return True
        if not board: return False

        def dfs(r, c, index, path):
            if index == len(word): return True
            if r not in range(len(board)): return False
            if c not in range(len(board[0])): return False
            if (r, c) in path: return False

            path.add((r, c))
            res = False
            if board[r][c] == word[index]:
                res = dfs(r + 1, c, index + 1, path) or dfs(r - 1, c, index + 1, path) or dfs(r, c + 1, index + 1, path) or dfs(r, c - 1, index + 1, path)

            path.remove((r, c))
            return res


        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0, set()): return True

        return False