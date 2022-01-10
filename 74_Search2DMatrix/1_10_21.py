class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        s, e = 0, len(matrix) - 1
        while s + 1 < e:
            m = (s + e) // 2
            if matrix[m][0] == target:
                return True
            if matrix[m][0] > target:
                e = m
            else:
                s = m
        if matrix[s][0] <= target < matrix[e][0]:
            return self.binarySearch(matrix[s], target)
        return self.binarySearch(matrix[e], target)
    
    def binarySearch(self, nums:List[int], target:int) -> bool:
        s, e = 0, len(nums) - 1
        while s <= e:
            m = (s + e) // 2
            if nums[m] == target:
                return True
            if nums[m] > target:
                e = m - 1
            else:
                s = m + 1
        return False