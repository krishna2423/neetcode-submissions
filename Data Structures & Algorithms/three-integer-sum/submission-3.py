class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # nlogn
        # [-4, -1, -1, 0, 1, 2]
        triples = []
        for i in range(len(nums)):
            target = -nums[i]
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # skip duplicate nums[i]
            p1 = i + 1
            p2 = len(nums) - 1
            while p1 < p2:
                if nums[p1] + nums[p2] == target:
                    triples.append([nums[i], nums[p1], nums[p2]])
                    p1 += 1
                    p2 -= 1
                    # skip duplicates
                    while p1 < p2 and nums[p1] == nums[p1 - 1]:
                        p1 += 1
                    while p1 < p2 and nums[p2] == nums[p2 + 1]:
                        p2 -= 1
                elif nums[p1] + nums[p2] < target:
                    p1 += 1
                else:
                    p2 -= 1
        return triples

