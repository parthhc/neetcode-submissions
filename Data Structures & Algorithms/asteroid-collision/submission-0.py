class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for ast in asteroids:
            if not stack or ast > 0: 
                stack.append(ast)
                continue

            while stack and abs(stack[-1]) < abs(ast) and stack[-1] > 0:
                stack.pop()

            if stack and stack[-1] == ast * -1:
                stack.pop()
                continue
            elif not stack or stack[-1] < 0:
                stack.append(ast)
                continue
        
        
        return stack