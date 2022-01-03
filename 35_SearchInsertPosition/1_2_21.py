# faster than 5.71%

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        start = 0
        end = len(nums) - 1
        while start < end - 1:
            mid = math.floor((start + end) / 2)
            if target > nums[mid]:
                start = mid
            elif target < nums[mid]:
                end = mid
            else:
                return mid
        if target <= nums[start]:
            return start
        elif target <= nums[end] and target > nums[start]:
            return end
        else:
            return end + 1