class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                curr_val = stack.pop()
                ans[curr_val[1]] = i - curr_val[1]

            stack.append([temperatures[i], i])

        return ans