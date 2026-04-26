from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            graph[course].append(pre)
        
        # cycle detection
        visited = set()   # fully processed nodes
        
        def dfs(course):
            if course in visited:
                return False
            if graph[course] == []:
                return True
            
            visited.add(course)
            for pre in graph[course]:
                if not dfs(pre):
                    return False
            visited.remove(course)
            graph[course] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
