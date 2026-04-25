class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix = list(accumulate(nums))
        min_prefix = min(prefix)
        return max(1 - min_prefix, 1)