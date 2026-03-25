class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        ans = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                    ans[i][j] = 1 - image[i][n - j - 1]
        return ans