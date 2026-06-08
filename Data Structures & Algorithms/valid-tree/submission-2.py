class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {i: [] for i in range(n)}
        
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)

        seen = set()

        def dfs(node, parent):
            if node in seen: return False

            nei = graph[node]
            seen.add(node)
            for n in nei:
                if n == parent: continue
                if not dfs(n, node):
                    return False
            
            return True

        res = dfs(0, -1)
        
        if len(seen) != n: return False

        return res
