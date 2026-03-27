class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        total = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] != grid[i][i] and grid[i][j] != grid[i][n - i - 1]:
                    total += grid[i][j]
                    if grid[i][i] != 0 and grid[i][n - i - 1] != 0 and total == 0:
                        return True
        return False