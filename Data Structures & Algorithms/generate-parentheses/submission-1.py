class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(openB, closeB, stack):
            if openB == closeB == n:
                res.append("".join(stack))
                stack = []
                return

            if openB < n:
                stack.append('(')
                backtrack(openB + 1, closeB, stack)
                stack.pop()

            if closeB < openB:
                stack.append(')')
                backtrack(openB, closeB + 1, stack)
                stack.pop()

        backtrack(0, 0, [])

        return res
