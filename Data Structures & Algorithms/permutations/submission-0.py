class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        used = [False] * len(nums)
        def dfs(curr, rem):
            if len(curr) == len(nums):
                result.append(curr.copy())
                return
            else:
                for i in range(len(rem)):
                    if used[i]:
                        continue

                    curr.append(rem[i])
                    used[i] = True
                    dfs(curr, rem)
                    curr.pop()
                    used[i] = False
        
        dfs([], nums)
        return result
