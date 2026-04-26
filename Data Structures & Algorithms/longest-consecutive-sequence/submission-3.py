class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: 
            return 0
        set_nums = set(nums)
        starting = []

        for num in nums:
            if num - 1 in set_nums:
                continue
            starting.append(num)
        
        max_count = 0
        for start in starting:
            count = 1
            while start + 1 in set_nums:
                count += 1
                start = start + 1
            max_count = max(count, max_count)
        
        return max_count

            
