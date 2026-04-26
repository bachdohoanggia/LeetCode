class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        n, m = len(grid), len(grid[0])
        temp = []
        for i in range(n):
            for j in range(m):
                temp.append(grid[i][j])

        N = len(temp)
        prefix = [1] * N
        for i in range(1, N):
            prefix[i] = prefix[i - 1] * temp[i - 1] % MOD
            
        suffix = [1] * N
        for i in range(N - 2, -1, -1):
            suffix[i] = suffix[i + 1] * temp[i + 1] % MOD
        
        res = [(prefix[i] * suffix[i]) % MOD for i in range(N)]

        ans = []
        idx = 0
        for i in range(n):
            row = []
            for j in range(m):
                row.append(res[idx])
                idx += 1
            ans.append(row)
        return ans