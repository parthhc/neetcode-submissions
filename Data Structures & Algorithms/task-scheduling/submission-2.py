class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = [0] * 26
        for task in tasks:
            counter[ord(task)- ord('A')] += 1
        
        counter.sort(reverse=True)
        max_task = counter[0]
        idle_time = (max_task - 1) * n
        
        for i in range(1, len(counter)):
            idle_time -= min(counter[i], max_task - 1)

        return len(tasks) + idle_time if idle_time >= 0 else len(tasks)

