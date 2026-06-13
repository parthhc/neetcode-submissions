class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i: [] for i in range(n)}

        for key, value in edges:
            graph[key].append(value)
            graph[value].append(key)

        
        visited = set()
        res = 0

        def dfs(i):
            if i in visited: return
            visited.add(i)

            for nei in graph[i]:
                dfs(nei)

        for i in range(n):
            if i not in visited:
                dfs(i)
                res += 1

        return res
            
