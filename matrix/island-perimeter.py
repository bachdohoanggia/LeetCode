class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        land_count = 0
        count = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    land_count += 1
                    for di, dj in directions:
                        ni = i + di
                        nj = j + dj
                        if 0 <= ni < row and 0 <= nj < col and grid[ni][nj] == 1:
                            count += 1
        return land_count*4 - count