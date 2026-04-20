class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0 for i in range(len(temperatures))]

        for i in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                temp, pos = stack.pop()
                res[pos] = i - pos

            stack.append((temperatures[i], i))

        return res
            
