class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        freq = Counter()
        pair = 0
        for a, b in dominoes:
            keys = (min(a, b), max(a,b))
            pair += freq[keys]
            freq[keys] += 1
        return pair