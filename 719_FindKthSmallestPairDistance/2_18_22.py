class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def less_than(distance):
            n = len(nums)
            count = j = 0
            for i in range(0, n-1):
                while j < n and nums[j] - nums[i] <= distance:
                    j += 1
                count += j - i - 1
            return count
        
   
        nums.sort()
        s,e = 0, nums[-1] - nums[0]
        while s <= e:
            m = (s + e) // 2
            if less_than(m) < k:
                s = m + 1
            else:
                e = m - 1
        return s