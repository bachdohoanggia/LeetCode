class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        rows = [0] * m
        cols = [0] * n
        count = 0
        for i in range(m):
            for j in range(n):
               rows[i] += mat[i][j]
               cols[j] += mat[i][j]
        for i in range(m):
            for j in range(n):
                if rows[i] == 1 and cols[j] == 1 and mat[i][j] == 1:
                    count += 1
        return count