class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        lp = len(p)
        ls = len(s)
        window = Counter(s[:len(p)])
        res = [0] if (window == Counter(p)) else []
        for right in range(lp, ls):
            window[s[right]] += 1
            window[s[right - lp]] -= 1
            if window == Counter(p):
                res.append(right - lp + 1)
        return res