class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        total = 0
        for i in range(n):
            for j in range(n):
                if i == j and i == n - j - 1:
                    if grid[i][j] == 0:
                        return False
                elif i != j and i != n - j - 1:
                    if grid[i][j] != 0:
                        return False
        return True