class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums.sort()

        # -4 -1 -1 0 1 2  

        for i in range(len(nums) - 1):
            num = nums[i]

            target = -1 * num
            left = i + 1
            right = len(nums) - 1

            while left < right:
                if nums[left] + nums[right] == target:
                    result.add((num, nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else: 
                    left += 1
        result = list(result)
        return [list(t) for t in result]

        

        

