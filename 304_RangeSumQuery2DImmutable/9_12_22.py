class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.sum = {}
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                add = matrix[row][col]
                if (row,col-1) in self.sum:
                    add = add + self.sum[(row,col-1)]
                if (row-1,col) in self.sum:
                    add = add + self.sum[(row-1, col)]
                if (row-1,col-1) in self.sum:
                    add = add - self.sum[(row-1,col-1)]
                self.sum[(row, col)] = add

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = self.sum[(row2, col2)]
        if (row1-1, col2) in self.sum:
            res = res - self.sum[(row1-1, col2)]
        if (row2,col1-1) in self.sum:
            res = res - self.sum[(row2,col1-1)]
        if (row1-1,col1-1) in self.sum:
            res = res + self.sum[(row1-1,col1-1)]
        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)