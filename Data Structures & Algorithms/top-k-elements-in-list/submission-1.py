class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return None
        # put everything in a list of buckets with frequency i
        result = []
        buckets = [[] for _ in range(len(nums) + 1)]

        freq = {}
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        
        for key,val in freq.items():
            buckets[val].append(key)
        
        i = len(nums)
        while i >= 0:
            if len(buckets[i]) + len(result) <= k:
                result.extend(buckets[i])
            else:
                while len(result) < k and buckets[i]:
                    result.append(buckets[i].pop())
            i -= 1
        return result


        