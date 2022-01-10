# binary search

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix), len(matrix[0])
        l, r = 0, m-1
        while l < r:
            mid = (l+r+1)//2
            if matrix[mid][0] > target:
                r = mid - 1
            else:
                l = mid
        row = l
        l, r = 0, n-1
        while l < r:
            mid = (l+r+1)//2
            if matrix[row][mid] > target:
                r = mid -1
            else:
                l = mid
        return matrix[row][l] == target   


# loop

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        temp = 0
        for i in range(1, m):
            if(target <= matrix[i][n-1] and target > matrix[i-1][n-1]):
                temp = i
        for j in range(n):
            if(target == matrix[temp][j]):
                return True
        return False
        