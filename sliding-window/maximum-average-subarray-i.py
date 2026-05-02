class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        res = []
        if n == 1:
            return nums[0]
        for r in range(k, n):
            res.append(sum(nums[r-k: r])/k)
        return max(res)