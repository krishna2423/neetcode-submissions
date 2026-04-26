class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        L = 0 
        pop_ids = []
        for R in range(1, len(nums)):
            if nums[R] == nums[L]:
                pop_ids.append(R)
            elif nums[R] != nums[L]:
                L = R
                continue
        
        print(pop_ids)
        k = len(nums) - len(pop_ids)
        
        for i in range(len(pop_ids) - 1, -1, -1):
            nums.pop(pop_ids[i])
        
        return k
        