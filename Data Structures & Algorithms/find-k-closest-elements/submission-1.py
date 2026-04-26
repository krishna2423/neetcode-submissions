class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        mod = []
        for e in arr:
            d = abs(x - e)
            mod.append(d)
        # sliding window across the sums
        res = 0
        curr = sum([mod[i] for i in range(k)])
        minimum = curr
        for i in range(k, len(arr)):
            curr -= mod[i - k]
            curr += mod[i]
            if curr < minimum:
                res = i - k + 1
                minimum = curr
        return [arr[i] for i in range(res, res + k)]