class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def enough(distance) -> bool:  # two pointers
            count, i, j = 0, 0, 0
            while i < n or j < n:
                while j < n and nums[j] - nums[i] <= distance:
                    j += 1
                count += j - i - 1
                i += 1
            return count >= k

        nums.sort()
        n = len(nums)
        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = left + (right - left) // 2
            if not enough(mid):
                left = mid + 1
            else:
                right = mid
        return left


def pairs(self, nums, x):
        pairs, i = 0, 0
        for j in range(len(nums)):
            while nums[j] - nums[i] > x:
                i = i+1
            pairs = pairs + (j-i)
        return pairs
...
if pairs < k: s = m+1
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        if not nums:
            return -1
        
        nums.sort()
        start, end = 0, nums[-1] - nums[0]
        while start + 1 < end:
            mid = (start + end) // 2
            if self.is_possible(nums, mid) < k:
                start = mid
            else:
                end = mid
        
        if self.is_possible(nums, start) >= k:
            return start
        
        if self.is_possible(nums, end) >= k:
            return end
        
        return -1       
        
    def is_possible(self, nums, diff):
        i = res = 0
        for j in range(1, len(nums)):
            while nums[j] - nums[i] > diff:
                i += 1
            
            res += j - i
            
        return res # num of pair <= diff 
            