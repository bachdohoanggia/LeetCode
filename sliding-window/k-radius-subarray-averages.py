class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        avg = [-1] * n
        
        if k == 0:
            return nums
        
        prefix = list(accumulate(nums))
        for i in range(k, n - k):
            total = prefix[i + k] - (prefix[i - k - 1] if i > k else 0)
            avg[i] = total // (2*k + 1)
        return avg