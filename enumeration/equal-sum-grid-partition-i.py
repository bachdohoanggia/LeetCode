class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        total = sum(sum(row) for row in grid)
        row_sum, col_sum = 0, 0

        if total % 2 != 0:
            return False
            
        for i in range(m - 1):
            row_sum += sum(grid[i])
            if row_sum == total / 2:
                return True

        for j in range(n - 1):
            col_sum += sum(row[j] for row in grid)
            if col_sum == total / 2:
                return True

        return False

        
                 