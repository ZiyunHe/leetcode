class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        N = len(matrix)
        left, right = matrix[0][0], matrix[-1][-1]
        
        def less_than(mid):
            count = 0
            row, col = 0, N - 1
            while row < N and col >= 0:
                if matrix[row][col] <= mid:
                    count += col + 1
                    row += 1                    
                else:
                    col -= 1
            return count
        
        while left <= right:
            mid = left + (right - left) //2
            print(left,right, mid)
            if (less_than(mid) < k): left = mid + 1
            else: right = mid - 1
        return left