class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def dfs(r, c):
            if not (0 <= r < len(board)): return
            if not (0 <= c < len(board[0])): return
            if board[r][c] == 'X' or board[r][c] == 'S': return

            board[r][c] = 'S'

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        for r in range(len(board)):
            if board[r][0] == 'O':
                dfs(r, 0)

            if board[r][len(board[0]) - 1] == 'O':
                dfs(r, len(board[0]) - 1)

        for c in range(len(board[0])):
            if board[0][c] == 'O':
                dfs(0, c)
            
            if board[len(board) - 1][c] == 'O':
                dfs(len(board) - 1, c)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'S':
                    board[r][c] = 'O'

        
