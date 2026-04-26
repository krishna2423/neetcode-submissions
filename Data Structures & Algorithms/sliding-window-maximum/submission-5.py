import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """if k >= len(nums):
            return [max(nums)]
        max_array = []
        l = 0
        for r in range(k, len(nums) + 1):
            max_array.append(max(nums[l:r]))
            l += 1
        return max_array"""
        max_heap = [(-x, i) for i, x in enumerate(nums[0:k])]
        heapq.heapify(max_heap)
        max_array = [-max_heap[0][0]]
        l = 0
        for r in range(k, len(nums)):
            heapq.heappush(max_heap, (-nums[r], r))
            elem = max_heap[0]
            while elem[1] <= l:
                heapq.heappop(max_heap)
                elem = max_heap[0]
            max_array.append(-elem[0])
            l += 1
        return max_array
            
