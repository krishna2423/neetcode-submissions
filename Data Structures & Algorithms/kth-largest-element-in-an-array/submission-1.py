import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        heapq.heapify(heap)
        i = 0
        while i < len(nums):
            heapq.heappush(heap, nums[i])
            if len(heap) > k:
                heapq.heappop(heap)
            i += 1
        return heapq.heappop(heap)