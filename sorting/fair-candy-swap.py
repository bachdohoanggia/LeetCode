class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        bob_set = set(bobSizes)
        for x in aliceSizes:
            y = x - (sumA - sumB) / 2
            if y in bob_set:
                return [x, y]