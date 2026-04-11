class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sumA = sum(aliceSizes)
        sumB = sum(bobSizes)
        diff = (sumA - sumB) / 2
        
        for x in aliceSizes:
            y = x - diff
            if y in set(bobSizes):
                return [x, y]