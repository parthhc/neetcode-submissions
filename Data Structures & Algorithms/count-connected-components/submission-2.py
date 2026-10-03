class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i: [] for i in range(n)}

        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)

        seen = set()

        def dfs(node):
            if node in seen: return 
            seen.add(node)
            
            for nei in graph[node]:
                dfs(nei)
        
        res = 0
        for i in range(n):
            if i not in seen:
                dfs(i)
                res += 1

        return res