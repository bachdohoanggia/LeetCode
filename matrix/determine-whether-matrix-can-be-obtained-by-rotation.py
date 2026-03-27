class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        ans = [[0] * n for _ in range(n)]
        for _ in range(4):
            for i in range(n):
                for j in range(n):
                    ans[i][j] = mat[n - i - 1][j]
                    if ans == target:
                        return True
        return False