import heapq
class MedianFinder:

    def __init__(self):
        self.largeheap = []
        self.smallheap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.smallheap, -num)
        heapq.heappush(self.largeheap, -heapq.heappop(self.smallheap))

        if len(self.largeheap) > len(self.smallheap):
            heapq.heappush(self.smallheap, -heapq.heappop(self.largeheap))

    def findMedian(self) -> float:
        if len(self.smallheap) > len(self.largeheap):
            return -self.smallheap[0]
        return (-self.smallheap[0] + self.largeheap[0]) / 2

