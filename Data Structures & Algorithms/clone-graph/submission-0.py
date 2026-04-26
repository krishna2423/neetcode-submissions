"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        hashmap = {None: None}

        queue = deque()
        visited = set()
        queue.append(node)
        visited.add(node)
        #populate the hashmap with copied nodes
        while queue:
            for i in range(len(queue)):
                cur = queue.popleft()
                # copy the node
                hashmap[cur] = Node(cur.val)

                for n in cur.neighbors:
                    if n not in visited:
                        queue.append(n)
                        visited.add(n)

        # connect the nodes in the hashmap
        queue = deque()
        visited = set()
        queue.append(node)
        visited.add(node)
        while queue:
            for i in range(len(queue)):
                cur = queue.popleft()
                # copy the neighbors
                ns = []
                for n in cur.neighbors:
                    ns.append(hashmap[n])
                    if n not in visited:
                        queue.append(n)
                        visited.add(n)
                        
                hashmap[cur].neighbors = ns
        return hashmap[node]


        