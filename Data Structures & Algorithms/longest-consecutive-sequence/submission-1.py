class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        set_nums = set(nums) # n
        starting = []
        

        for num in nums: # n
            if num - 1 not in set_nums:
                starting.append(num) 
        
        lengths = [1 for x in starting]
        for i in range(len(starting)):
            s = starting[i]
            while True:
                s += 1
                if s not in set_nums:
                    break
                lengths[i] += 1
        return max(lengths)
