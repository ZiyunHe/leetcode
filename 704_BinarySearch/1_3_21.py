class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s, e = 0, len(nums) - 1
        while s <= e:
            mid = (s + e) // 2
            if target < nums[mid]:
                e = mid - 1
            elif target > nums[mid]:
                s = mid + 1
            else:
                return mid
        return -1