class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for k in (Counter(t) - Counter(s)).keys():
            return k