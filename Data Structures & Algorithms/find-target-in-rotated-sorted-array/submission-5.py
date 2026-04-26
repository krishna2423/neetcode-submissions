class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[l] < nums[r]:
                if nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            else: # (left is greater than right)
                # if we're on the left side of the partition check if target can be in between left and mid
                if nums[mid] >= nums[l]:
                    if nums[mid] > target and nums[l] <= target:
                        r = mid - 1
                    else:
                        l = mid + 1
                elif nums[mid] <= nums[r]: # if we're on the right side of the partition check if the target can be in between mid and right
                    if nums[mid] < target and nums[r] >= target:
                        l = mid + 1
                    else:
                        r = mid - 1                
        return -1