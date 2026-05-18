class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}

        for course, preReq in prerequisites:
            graph[course].append(preReq)

        confirmed = set()
        visited = set()

        def dfs(i):
            if i in visited: return False
            if i in confirmed: return True

            visited.add(i)
            for course in graph[i]:
                if not dfs(course):
                    return False
            visited.remove(i)
            confirmed.add(i)

            return True



        for i in range(numCourses):
            if not dfs(i):
                return False

        return True