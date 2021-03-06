class Solution(object):
    def findKthNumber(self, m, n, k):
        def enough(x):
            count = 0
            for i in range(1, m+1):
                count += min(x // i, n)
            return count >= k

        lo, hi = 1, m * n
        while lo < hi:
            mi = (lo + hi) / 2
            if not enough(mi):
                lo = mi + 1
            else:
                hi = mi
        return lo


class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def less_than(mid:int) -> int:
            count = 0
            for i in range(1, m+1):
                count += min(mid // i, n)
            return count

        s, e = 0, m*n - 1
        while s<=e:
            mid = (s+e) // 2
            if less_than(mid) < k:
                s = mid + 1
            else:
                e = mid - 1
        return s


# faster
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        if m > n:
            m, n = n, m
        
        def nums_le(x):
            q = x // n
            res = q * n
            for i in range(q+1, m+1):
                res += x // i
            return res
        
        lo, hi = 1, m * n
        
        while lo < hi:
            mid = (lo + hi) // 2
            if nums_le(mid) < k:
                lo = mid + 1
            else:
                hi = mid
                
        return lo