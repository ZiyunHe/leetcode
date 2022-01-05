class Solution:

    # This solution does NOT work

    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return -1
        s, e = 0, len(nums) - 1
        if nums[s] < nums[e] or len(nums) == 1:
            return nums[s]
        while s <= e:
            m = (s+e) // 2
            if m + 1 < len(nums) and nums[m+1] < nums[m]:
                s = m
                break
            if nums[s] >= nums[e]:
                s = m + 1
            else:
                e = m - 1
        print(s, e)
        if s == len(nums):
            return nums[0]
        return nums[s+1]