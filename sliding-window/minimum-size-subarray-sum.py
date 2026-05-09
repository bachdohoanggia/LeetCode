class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        min_len = inf if sum(nums) >= target else 0
        left = 0
        window = []
        for right in range(n):
            window.append(nums[right])
            while sum(window) > target:                
                window.remove(nums[left])
                left += 1
                min_len = min(min_len, right - left + 1)
        return min_len