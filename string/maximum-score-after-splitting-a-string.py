class Solution:
    def maxScore(self, s: str) -> int:
        ans = 0
        for i in range(1, len(s)):
            c1 = Counter(s[:i])
            c2 = Counter(s[i:])
            ans = max(ans, c1['0'] + c2['1'])
        return ans
                        