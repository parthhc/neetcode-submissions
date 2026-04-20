class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # make a map for course to prereqs
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        def dfs(courseNum, path):
            if courseNum in path:
                return False
            if preMap[courseNum] == []:
                return True
            path.add(courseNum)
            
            for c in preMap[courseNum]:
                if not dfs(c, path):
                    return False
            
            path.remove(courseNum)
            return True
            
        
        for c in range(numCourses):
            if not dfs(c, set()):
                return False
        
        return True