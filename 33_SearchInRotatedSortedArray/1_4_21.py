class Solution:

    # this solution does NOT work

    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        s, e = 0, len(nums) - 1
        while s <= e:
            m = (s + e) // 2
            if m + 1 < len(nums) and nums[m + 1] < nums[m]:
                s = m + 1

            # first try does NOT work, Time Limit Exceeded
            # 'elif m - 1 > -1 and nums[m - 1] < nums[m]:'
            # because forget every else case
            # so changed to 'else' statement:
            else:

                e = m - 1
        left = self.bs(nums[0:s], target)
        right = self.bs(nums[s:], target)
        if not left == -1:
            return left
        if not right == -1:
            return len(nums[0:s]) + right
        return -1
    
    def bs(self, nums:List[int], target:int) -> int:
        if not nums:
            return -1
        s, e = 0, len(nums) - 1
        while s <= e:
            m = (s + e) // 2
            if nums[m] == target:
                return m
            if nums[m] < target:
                s = m + 1
            else:
                e = m - 1
        return -1