class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        tr_in = [0] * (n+1)
        tr_out = [0] * (n+1)
        for a, b in trust:
            tr_out[a] += 1
            tr_in[b] += 1
        for i in range(1, n + 1):
            if tr_out[i] == 0 and tr_in[i] == n-1:
                return i
        return -1