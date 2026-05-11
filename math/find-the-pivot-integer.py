class Solution:
    def pivotInteger(self, n: int) -> int:
        prefix = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix[i] = i*(i + 1) / 2 
        for i in range(1, n + 1):
            if prefix[i] == n*(n+1)/2 - prefix[i - 1]:
                return i
        return -1