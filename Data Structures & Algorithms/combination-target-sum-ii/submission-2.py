class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        def track(i, curr_sum, curr):
            if curr_sum == target:
                result.append(curr)
                return
            elif i >= len(candidates) or curr_sum > target:
                return
            else:
                # use the current 
                track(i + 1, curr_sum + candidates[i], curr + [candidates[i]])
                # don't use the current
                while i + 1 < len(candidates) and candidates[i + 1] == candidates[i]:
                    i += 1
                track(i + 1, curr_sum, curr)  
        track(0, 0, [])
        return result