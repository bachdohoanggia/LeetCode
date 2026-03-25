class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans = 0
        n = len(mat)
        for i in range(n):
            ans += mat[i][i] + mat[i][n - i - 1]
        if n % 2 != 0:
            ans -= mat[int(n/2)][int(n/2)]
        return ans
