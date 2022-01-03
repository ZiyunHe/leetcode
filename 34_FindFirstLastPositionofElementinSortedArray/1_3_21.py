class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        # self.
        return [self.binarySearch(nums, target, True), self.binarySearch(nums, target, False)]
    
    def binarySearch(self, nums: List[int], target:int, is_left: bool) -> int:
        s, e = 0, len(nums) - 1
        while s <= e:
            mid = (s + e) // 2
            if target < nums[mid] or (is_left and (mid - 1) > -1 and target == nums[mid - 1]):
                e = mid - 1
            elif target > nums[mid] or (not is_left and (mid + 1) < len(nums) and target == nums[mid + 1]):
                s = mid + 1
            else:
                return mid
        return -1