class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myset = set()
        for num in nums:
            myset.add(num)
        if len(nums) > len(myset): 
            return True
        else: 
            return False
        