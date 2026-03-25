class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans_diag1 = 0
        ans_diag2 = 0
        ans = 0
        n = len(mat)
        for i in range(n):
            ans_diag1 += mat[0][i]
        for i in range(n):
            mat.reverse()
        for i in range(n):
            ans_diag2 += mat[0][i]
        if n % 2 == 0:
            ans = ans_diag1 + ans_diag2
        else:
            ans = ans_diag1 + ans_diag2 - mat[int(n/2)][int(n/2)]
        return ans
