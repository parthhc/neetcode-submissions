class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(r, c, index, path):
            if index == len(word): return True
            if r not in range(len(board)): return
            if c not in range(len(board[0])): return
            if (r, c) in path: return

            path.add((r,c))

            if board[r][c] == word[index]:
                res = dfs(r + 1, c, index + 1, path) or dfs(r - 1, c, index + 1, path) or dfs(r, c + 1, index + 1, path) or dfs(r, c - 1, index + 1, path)

                if res: return True
            
            path.remove((r,c))



        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r, c, 0, set()): return True

        return False