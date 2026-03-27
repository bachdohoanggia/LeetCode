class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        ans = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                ans[j][n - i - 1] = mat[i][j]
        for _ in range(4):
            if ans == target:
                return True
        return False