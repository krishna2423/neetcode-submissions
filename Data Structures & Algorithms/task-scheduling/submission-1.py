import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        hashmap = {}
        for c in tasks:
            if c in hashmap:
                hashmap[c] += 1
            else:
                hashmap[c] = 1
        heap = [-x[1] for x in hashmap.items()]
        heapq.heapify(heap)
        queue = deque([])
        while heap or queue:
            if queue:
                if queue[0][1] == time:
                    heapq.heappush(heap, queue.popleft()[0])
            if heap:
                first = heapq.heappop(heap)
                if first + 1 < 0:
                    queue.append((first + 1, time + n + 1))
            time += 1   
                
        return time

