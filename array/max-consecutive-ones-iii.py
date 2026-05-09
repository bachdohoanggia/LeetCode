class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = 0
        total = 0
        max_len = 0
        for right in range(n):
            total += nums[right]
            while (right - left + 1) - total > k:
                total -= nums[left]
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len

