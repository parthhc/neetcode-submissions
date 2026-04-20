class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            res = None
            if token == '+':
                n1 = stack.pop()
                n2 = stack.pop()
                res = n2 + n1
            elif token == '-':
                n1 = stack.pop()
                n2 = stack.pop()
                res = n2 - n1
            elif token == '/':
                n1 = stack.pop()
                n2 = stack.pop()
                res = int(float(n2) / n1)
            elif token == '*':
                n1 = stack.pop()
                n2 = stack.pop()
                res = n2 * n1
            else:
                res = int(token)

            stack.append(res)

        return stack.pop()