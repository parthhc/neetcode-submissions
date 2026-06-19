class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(numCourses)}

        for c1, c2 in prerequisites:
            graph[c1].append(c2)

        res, visit, cycle = [], set(), set()

        def dfs(course):
            if course in visit: return True
            if course in cycle: return False

            cycle.add(course)
            for prereq in graph[course]:
                if not dfs(prereq): return False
            cycle.remove(course)
            visit.add(course)
            res.append(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        
        return res