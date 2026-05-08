class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        total = sum(cardPoints)
        window = sum(cardPoints[: n - k])
        min_sum = window
        for right in range(n - k, n):
            window = window + cardPoints[right] - cardPoints[right - n + k]
            min_sum = min(min_sum, window)
        return total - min_sum
        
