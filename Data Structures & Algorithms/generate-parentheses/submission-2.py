class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        stack = []
        def dfs(openB, closeB):
            if closeB == openB == n: 
                res.append(''.join(stack))
                return
            if closeB > openB: return
            if openB > n: return
            
            stack.append('(')
            dfs(openB + 1, closeB)
            stack.pop()

            stack.append(')')
            dfs(openB, closeB + 1)
            stack.pop()




        stack.append('(')
        dfs(1, 0)

        return res
            
            
