class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        if not arr:
            return -1
        s, e = 0, len(arr) - 1
        while s <= e:
            m = (s + e) // 2
            if arr[m-1] < arr[m] and arr[m+1] < arr[m]:
                return m
            if arr[m] <= arr[m+1]:
                s = m + 1
            else:
                e = m - 1
        return -1