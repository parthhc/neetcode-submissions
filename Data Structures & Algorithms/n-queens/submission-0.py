class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        queens_pos = []
        stack = []
        res = []
        
        def can_add(queen_pos):
            for pos in queens_pos:
                if queen_pos[0] == pos[0]: return False
                if queen_pos[1] == pos[1]: return False
                if pos[0] - pos[1] == queen_pos[0] - queen_pos[1]:
                    return False
                if pos[0] + pos[1] == queen_pos[0] + queen_pos[1]:
                    return False
            
            return True

        def backtrack(itr):
            if itr == n:
                res.append(stack[:])
                return
            
            row = ["." for _ in range(n)]
            for i in range(n):
                if not can_add((itr, i)): continue
                
                row[i] = "Q"
                row_str = "".join(row)

                queens_pos.append((itr, i))
                stack.append(row_str)

                backtrack(itr + 1)

                queens_pos.pop()
                stack.pop()

                row[i] = "."

        
        backtrack(0)
        return res

                
