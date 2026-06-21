class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        c = n // 2
        total = 0
        for i in range(n):
            total += mat[i][i] + mat[i][n - i - 1]
        if n % 2 != 0:
            return total - mat[c][c]
        return total
