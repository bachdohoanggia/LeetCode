class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        def rotate_90(matrix):
            ans = [[0] * n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    ans[j][n - i - 1] = matrix[i][j]
            return ans

        curr = mat
        for _ in range(4):
            if curr == target:
                return True
            curr = rotate_90(cur)
        return False
