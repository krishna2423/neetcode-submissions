class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = 0 
        ones = 0 
        twos = 0 
        for x in nums:
            if x == 0:
                zeros += 1
            elif x == 1:
                ones += 1
            else:
                twos += 1
        zero_index = 0 
        ones_index = zeros
        twos_index = zeros + ones

        for i in range(0, ones_index):
            nums[i] = 0
        for i in range(ones_index, twos_index):
            nums[i] = 1
        for i in range(twos_index, len(nums)):
            nums[i] = 2
        