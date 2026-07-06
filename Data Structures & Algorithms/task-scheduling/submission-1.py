class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0] * 26

        for task in tasks:
            count[ord(task) - ord('A')] += 1

        count.sort()
        max_freq = count[25]
        idle = (max_freq - 1) * n

        for i in range(24, -1, -1):
            idle -= min(max_freq - 1, count[i])

        return max(idle, 0) + len(tasks)