from collections import defaultdict

class TimeMap:

    def __init__(self):
        self._timestamped_key_values = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        timestamped_values = self._timestamped_key_values[key]
        
        if not timestamped_values or timestamped_values[-1][1] != value:
            timestamped_values.append((timestamp, value))    

    def get(self, key: str, timestamp: int) -> str:
        timestamped_values = self._timestamped_key_values[key]
        
        if not timestamped_values or timestamped_values[0][0] > timestamp:
            return ""
        
        lo, hi = 0, len(timestamped_values) - 1
        
        while lo < hi:
            mid = (hi + lo + 1) // 2
            mid_timestamp = timestamped_values[mid][0]
            
            if mid_timestamp < timestamp:
                lo = mid
            elif mid_timestamp == timestamp:
                lo = hi = mid
            else:
                hi = mid - 1
        
        return timestamped_values[lo][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)