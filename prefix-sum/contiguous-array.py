class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        seen = {0: -1}
        max_len = 0
        prefix = 0
        for i, num in enumerate(nums):
            prefix += 1 if num == 1 else -1
            if prefix in seen:
                length = i - seen[prefix]
                max_len = max(max_len, length)
            else:
                seen[prefix] = i
        return max_len