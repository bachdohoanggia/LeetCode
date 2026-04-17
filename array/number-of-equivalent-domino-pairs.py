from collections import Counter
from typing import List

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        normal = []

        for d in dominoes:
            normal.append(tuple(sorted(d)))
        count = Counter(normal)

        result = 0
        for v in count.values():
            result += v * (v - 1) // 2
        
        return result