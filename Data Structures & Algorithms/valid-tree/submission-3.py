class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {i: [] for i in range(n)}
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        
        
        visited = set()
        
        def dfs(node, prev):
            if node in visited: return False

            visited.add(node)
            for nei in graph[node]:
                if nei == prev: continue
                if not dfs(nei, node):
                    return False

            return True
        
        res = dfs(0, -1)
        if len(visited) != n: return False
        return res