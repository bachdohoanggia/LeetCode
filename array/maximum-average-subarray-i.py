class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        pref = list(accumulate(nums))
        max_sum = pref[k - 1]
        for i in range(k, n):
            current = pref[i] - pref[i - k]
            max_sum = max(current / k, max_sum)
        return max_sum
        