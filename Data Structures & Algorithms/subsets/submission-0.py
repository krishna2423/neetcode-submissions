class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def getSizeSubsets(nums, size):
            # returns all subsets of a particular size and returns them in a list
            res = []
            def helper(i, curr):
                if len(curr) == size:
                    res.append(curr)
                    return
                if i >= len(nums):
                    return 
                
                else:
                    # use the current element 
                    helper(i + 1, curr + [nums[i]])
                    # skipping current element
                    helper(i + 1, curr)
            helper(0, [])
            return res


        result = [[]]
        for i in range(1, len(nums) + 1):
            sets = getSizeSubsets(nums, i)
            result.extend(sets)
        
        return result
        