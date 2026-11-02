class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def dfs(i, j):
            if i < 0 or i >= len(board): return
            if j < 0 or j >= len(board[0]): return
            if board[i][j] != 'O': return

            board[i][j] = 'S'
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)


        for i in range(len(board)):
            if board[i][0] == 'O':
                dfs(i, 0)

            if board[i][len(board[0]) - 1] == 'O':
                dfs(i, len(board[0]) - 1)

        for j in range(len(board[0])):
            if board[0][j] == 'O':
                dfs(0, j)

            if board[len(board) - 1][j] == 'O':
                dfs(len(board) - 1, j)

        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'S':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
