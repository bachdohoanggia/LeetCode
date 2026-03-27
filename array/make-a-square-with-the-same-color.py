class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        m = len(grid)
        for i in range(m-1):
            for j in range(m-1):
                count_B = 0
                for x in range(i, i + 2):
                    for y in range(j, j + 2):
                        if grid[x][y] == "B":
                            count_B += 1
                if count_B != 2:
                    return True
        return False