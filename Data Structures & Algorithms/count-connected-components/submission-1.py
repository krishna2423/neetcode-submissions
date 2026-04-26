class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0 
        graph = {i: [] for i in range(n)}
        for src, dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)
        visited = set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)

        for n in range(n):
            if n not in visited:
                res += 1
                dfs(n)
        return res

        
            

