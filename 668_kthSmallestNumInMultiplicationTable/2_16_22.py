class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def less_than(target):
            count = 0
            for i in range(1, m+1):
                count += min(n, target // i)
            return count
        
        s, e = 1, m*n
        while s<=e:
            mid = (s+e) // 2
            if less_than(mid) < k:
                s = mid+1
            else:
                e = mid-1
        return s
            