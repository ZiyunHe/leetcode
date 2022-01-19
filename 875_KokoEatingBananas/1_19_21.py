class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        s, e = 1, max(piles)
        while s < e:
            m = (s+e) // 2
            hours = self.eats(piles, h, m)
            if hours <= h:
                e = m
            elif hours > h:
                s = m + 1
        return s
                
    def eats(self, piles: List[int], h:int, target:int) -> int:
        total = 0
        for i in range (0,len(piles)):
            total += piles[i] // target
            # python syntax b if a > 10 else c
            total += 1 if piles[i] % target > 0 else 0
        return total