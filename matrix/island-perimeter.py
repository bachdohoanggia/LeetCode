class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        edge_count = 0
        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for i in range(row):
            for j in range(col):
                if grid[i][j] != 1:
                    continue
                edges = 4
                for di, dj in DIRS:
                    ni = i + di
                    nj = j + dj
                    if not (0 <= ni < row and 0 <= nj < col):
                        continue
                    if grid[ni][nj] == 1:
                        edges -= 1
                edge_count += edges

        return edge_count    