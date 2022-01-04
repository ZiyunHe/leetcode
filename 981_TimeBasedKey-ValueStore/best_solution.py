class TimeMap:

    def __init__(self):
        self.timestamps = collections.defaultdict(list)
        self.values = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timestamps[key].append(timestamp)
        self.values[key].append(value)
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.values:
            return ''
        idx = bisect.bisect_right(self.timestamps[key], timestamp)
        if idx == 0:
            return ''
        return self.values[key][idx-1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)