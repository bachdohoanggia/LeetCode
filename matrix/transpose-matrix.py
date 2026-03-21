class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        trans_mat = [[0] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                trans_mat[j][i] = matrix[i][j]
        return trans_mat

            
