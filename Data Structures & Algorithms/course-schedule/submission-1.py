from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        # create the adjacency list
        graph = {}
        for src, dst in prerequisites:
            if src not in graph:
                graph[src] = []
            if dst not in graph:
                graph[dst] = []
            graph[src].append(dst)
        
        # cycle detection
        visited = set()   # fully processed nodes
        path = set()      # current DFS recursion stack

        def dfs(course):
            if course in visited:
                return True
            if course in path:
                return False
            
            path.add(course)

            for p in graph[course]:
                if not dfs(p):
                    return False

            path.remove(course)
            visited.add(course)
            return True

        for c in graph.keys():
            if dfs(c) == False:
                return False

        return True 
