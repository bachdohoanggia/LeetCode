class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix = 0
        min_prefix = 0
        for num in nums:
            prefix += num
            min_prefix = min(min_prefix, prefix)
        return max(1 - min_prefix, 1)