class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)
        left = 0
        count = defaultdict(int)
        max_freq, max_len = 0, 0
        for right in range(n):
            count[answerKey[right]] += 1
            max_freq = max(max_freq, count[answerKey[right]])
            while (right - left + 1) - max_freq > k:
                count[answerKey[left]] -= 1
                left += 1
                max_freq = max(max_freq, count[answerKey[right]])
                
            max_len = max(max_len, right - left + 1)
        return max_len

