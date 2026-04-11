class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_in = [0] * (n + 1)
        trust_out = [0] * (n + 1)
        for a, b in trust:
            trust_out[a] += 1
            trust_in[b] += 1
        for i in range(1, n + 1):
            if trust_in[i] == n - 1 and trust_out[i] == 0:
                return i
        return -1