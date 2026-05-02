class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        window = sum(nums[:k])
        best_avg =  window/k
        for right in range(k, n):
            window = window + nums[right] - nums[right - k]
            best_avg = max(best_avg, window/k)
        return best_avg