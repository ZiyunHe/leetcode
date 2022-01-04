class Solution:

    # this solution does NOT work
    
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return -1
        s, e = 0, len(nums) - 1
        while s <= e:
            m = (s + e) // 2
            if m + 1 < len(nums) and nums[m + 1] < nums[m]:
                s = m
                break
            if nums[s] <= nums[m]:
                s = m + 1
            else:
                e = m - 1
        left = self.bs(nums[0:s+1], target)
        right = self.bs(nums[s+1:], target)
        return left or right
        return False
    
    def bs(self, nums:List[int], target:int) -> bool:
        if not nums:
            return False
        s, e = 0, len(nums) - 1
        while s <= e:
            m = (s + e) // 2
            if nums[m] == target:
                return True
            if nums[m] < target:
                s = m + 1
            else:
                e = m - 1
        return False