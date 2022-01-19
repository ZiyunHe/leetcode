class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        max_weight = max(weights)
        left, right = max(math.ceil(sum(weights)/days), max_weight), math.ceil(len(weights)/days)*max_weight
        while left < right:
            mid = (left+right)//2
            day_count = 1
            cap = mid
            for weight in weights:
                if cap >= weight:
                    cap -= weight
                else:
                    day_count += 1
                    cap = mid-weight
            
            if day_count > days:
                left = mid+1
            else:
                right = mid
        return left