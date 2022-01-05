class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums:
            return -1
        s, e = 0, len(nums) - 1
        while s < e - 1:
            m = (s + e) // 2
            if nums[m] > nums[m -1] and nums[m] > nums[m + 1]:
                return m
            if nums[m] < nums[m + 1]:
                s = m + 1
            else:
                e = m - 1
        if nums[s] >= nums[e]:
            return s
        if nums[s] < nums[e]:
            return e
        return -1