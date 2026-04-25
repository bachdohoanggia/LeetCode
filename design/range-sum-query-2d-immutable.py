class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        self.prefix = [[0] * (n) for _ in range(m)]
        for i in range(m):
            for j in range(n):
                rec1 = self.prefix[i-1][j] if i > 0 else 0
                rec2 = self.prefix[i][j-1] if j > 0 else 0
                rec3 = self.prefix[i-1][j-1] if (i > 0 and j > 0) else 0
                self.prefix[i][j] = rec1 + rec2 - rec3 + matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        rec1 = self.prefix[row1-1][col2] if row1 > 0 else 0
        rec2 = self.prefix[row2][col1-1] if col1 > 0 else 0
        rec3 = self.prefix[row1-1][col1-1] if (row1 > 0 and col1 > 0) else 0
        return self.prefix[row2][col2] - rec1 - rec2 + rec3


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)