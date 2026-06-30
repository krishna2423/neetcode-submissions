class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = [(timestamp, value)]
        else:
            self.hashmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""
        timestamps = self.hashmap[key]
        l, r = 0, len(timestamps) - 1
        res = ""
        while l <= r:
            m = (l + r) // 2  
            if timestamps[m][0] <= timestamp:
                res = timestamps[m][1]
                l = m + 1  
            else:
                r = m - 1
        return res
