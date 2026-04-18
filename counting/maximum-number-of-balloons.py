class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        ans = Counter(text)
        b = ans['b']
        a = ans['a']
        l = ans['l'] // 2
        o = ans['o'] // 2
        n = ans['n']

        return min(b, a, l, o, n)