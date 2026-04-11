class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        row = [0] * n
        col = [0] * m
        for i in range(m):
            for j in range(n):
                row[i] += mat[i][j]
                col[j] += mat[i][j]
        count = 0
        for i in range(m):
            for j in range(n):
                if row[i] == 1 and col[j] == 1 and mat[i][j] == 1:
                    count += 1
        return count