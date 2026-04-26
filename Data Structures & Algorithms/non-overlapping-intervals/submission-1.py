class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        intervals.sort(key=lambda x: x[0])

        res = 0 
        processed = []
        for start, end in intervals:
            if not processed:
                processed.append([start, end])
            else:
                if start < processed[-1][1]:
                    res += 1
                    if end < processed[-1][1]:
                        processed.pop()
                        processed.append([start, end])
                else:
                    processed.append([start, end])
        return res