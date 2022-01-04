class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return -1
        s, e = 0, len(nums) - 1
        # need <=
        # because [1]
        if nums[s] <= nums[e]:
            return nums[s]
        while s <= e:
            m = (s + e) // 2
            if m + 1 < len(nums) and nums[m] > nums[m + 1]:
                s = m
                break
            # need <= instead of =,
            # because [...1, 2...]
            #            s+m, e
            if nums[s] <= nums[m]:
                s = m + 1
            else:
                e = m - 1
        return min(nums[0], nums[s + 1])