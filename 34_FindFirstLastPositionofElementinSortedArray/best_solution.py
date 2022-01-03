class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        
        found = False
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                found = True
                break
        
        if not found:
            return [-1, -1]
            
        ans = [0, 0]
        for i in range(left, mid + 1):
            if nums[i] == target:
                ans[0] = i
                break
        for i in range(right, mid - 1, -1):
            if nums[i] == target:
                ans[1] = i
                break
        return ans