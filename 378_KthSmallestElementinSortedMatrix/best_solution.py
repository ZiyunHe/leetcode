class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        N = len(matrix)
        left, right = matrix[0][0], matrix[N - 1][N -1]
        
        def less_than(mid):
            count = 0
            row, col = N - 1, 0
            while row >= 0 and col < N:
                if matrix[row][col] <= mid:
                    count += row + 1
                    col += 1                    
                else:
                    row -= 1
            return count
        
        while left <= right:
            mid = left + (right - left) //2
            if (less_than(mid) < k): left = mid + 1
            else: right = mid - 1
        return left