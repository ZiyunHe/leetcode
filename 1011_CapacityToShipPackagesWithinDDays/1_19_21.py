class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        s, e = max(weights), sum(weights)
        while s < e:
            m = (s + e) // 2
            d = self.isViable(weights, m)
            if d <= days:
                e = m
            else:
                s = m + 1
        return s
    
    def isViable(self, weights: List[int], target:int) -> int:
        total = 1
        subsum = 0
        for i in range (0, len(weights)):
            subsum += weights[i]
            if subsum > target:
                subsum = weights[i]
                total += 1

        return total