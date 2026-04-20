class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for letter in s:
            if letter == '[' or letter == '(' or letter == '{':
                stack.append(letter)
                continue
            if not stack: return False
            if letter == ']' and stack.pop() != '[': return False
            elif letter == '}' and stack.pop() != '{': return False
            elif letter == ')' and stack.pop() != '(': return False

        if stack: return False
        
        return True
                