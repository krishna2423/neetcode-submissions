import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)
        for p in points:
            distance = math.sqrt((p[0] * p[0]) + (p[1] * p[1]))
            heapq.heappush(heap, (-distance, p))
            if len(heap) > k:
                heapq.heappop(heap)
        result = []
        while k > 0:
            item = heapq.heappop(heap)
            result.append(item[1])
            k -= 1
        return result
