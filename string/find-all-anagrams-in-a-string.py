class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        lp = len(p)
        ls = len(s)
        target = Counter(p)
        window = Counter(s[:len(p)])
        res = [0] if (window == target) else []
        for right in range(lp, ls):
            window[s[right]] += 1
            window[s[right - lp]] -= 1
            if window == target:
                res.append(right - lp + 1)
        return res