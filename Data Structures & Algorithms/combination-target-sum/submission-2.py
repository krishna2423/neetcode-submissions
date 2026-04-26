class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        res = set()
        def track(lst, pos, curr, curr_sum, target):
            if pos >= len(lst):
                return
            if curr_sum + lst[pos] > target:
                return 
            elif curr_sum + lst[pos] == target:
                curr.append(lst[pos])
                res.add(tuple(curr))
                return
            else:
                track(lst, pos, curr + [lst[pos]], curr_sum + lst[pos], target) # dont continue forward and add current position
                track(lst, pos + 1, curr + [lst[pos]], curr_sum + lst[pos], target) # continue forward and use current element
                track(lst, pos + 1, curr, curr_sum, target) # continue forward and don't use the past element
        track(nums, 0, [], 0, target)
        res = list(res)
        return [list(x) for x in res]
        """
        result = []
        def track(i, curr_sum, curr):
            if curr_sum > target or i >= len(nums):
                return
            elif curr_sum == target:
                result.append(curr)
            else:
                # check left
                track(i, curr_sum + nums[i], curr + [nums[i]])
                # check right
                track(i + 1, curr_sum, curr)
        
        track(0, 0, [])
        return result
