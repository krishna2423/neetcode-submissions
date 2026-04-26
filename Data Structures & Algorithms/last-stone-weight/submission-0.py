import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = -heapq.heappop(stones)
            second = -heapq.heappop(stones)
            if first != second:
                first = first - second
                heapq.heappush(stones, -first)
        if not stones:
            return 0
        else:
            return -heapq.heappop(stones)