import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)
        hashmap = {}
        distances = []
        for p in points:
            distance = math.sqrt((p[0] * p[0]) + (p[1] * p[1]))
            if distance not in hashmap:
                hashmap[distance] = []
            hashmap[distance].append(p)
            distances.append(distance)
        for d in distances:
            heapq.heappush(heap, -d)
            if len(heap) > k:
                heapq.heappop(heap)
        result = []
        while k > 0:
            key = -heapq.heappop(heap)
            val = hashmap[key]
            while k and val:
                result.append(val.pop())
                k -= 1
        return result
