class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqMap = {i: [] for i in range(numCourses)}

        for course, prereq in prerequisites:
            prereqMap[course].append(prereq)

        def dfs(course, visited):
            if course in visited: return False
            if prereqMap[course] == []: return True

            visited.add(course)

            for i in range(len(prereqMap[course])):
                if not dfs(prereqMap[course][i], visited):
                    return False
            
            visited.remove(course)
            return True

        for course in prereqMap.keys():
            if not dfs(course, set()): return False

        return True