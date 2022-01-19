class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)
        while start < end:
            k = (start+end)//2
            # if sum([(p-1) // k + 1 for p in piles]) <= h:
            if sum([-(p//-k) for p in piles]) <= h:
                end = k
            else:
                start = k+1
                
        return end

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        if len(piles) == h:
            return max(piles)
        
        s = sum(piles)
        l,r = (s - 1) // h + 1, (s - 1) // (h - len(piles)) + 1
        
        def isViable(cap):
            return sum((p-1)//cap + 1 for p in piles) <= h
        while l < r:
            
            m = (l + r) // 2
            if isViable(m):
                r = m
            else:
                l = m + 1
        return l
            