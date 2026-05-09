class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        min_len = inf
        total = 0
        left = 0
        for right in range(n):
            total += nums[right]
            while total >= target:      
                min_len = min(min_len, right - left + 1)          
                total -= nums[left]
                left += 1
                
        return min_len if min_len != inf else 0