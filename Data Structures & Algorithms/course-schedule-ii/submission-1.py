class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {c: set() for c in range(numCourses)}

        for c, prereq in prerequisites:
            graph[c].add(prereq)

        visited = set()
        res = []
        confirmed = set()
        def dfs(course):
            if course in confirmed: return True
            if course in visited: return False

            visited.add(course)
            for prereq in graph[course]:
                if not dfs(prereq):
                    return False

            visited.remove(course)
            confirmed.add(course)
            res.append(course)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []

        return res