class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {c: [] for c in range(numCourses)}
        rank = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            rank[course] += 1

        q = collections.deque()

        for i in range(len(rank)):
            if rank[i] == 0:
                q.append(i)

        res = []
        while q:
            course = q.popleft()
            res.append(course)
            for nei in graph[course]:
                rank[nei] -= 1
                if rank[nei] == 0:
                    q.append(nei)
            
        for r in rank:
            if r != 0:
                return []
        
        return res