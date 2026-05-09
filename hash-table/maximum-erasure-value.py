class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        ans = 0
        left = 0
        total = 0
        window = set()
        for digit in nums:
            while digit in window:
                window.remove(nums[left])
                total -= nums[left]
                left += 1
            window.add(digit)
            total += digit
            ans = max(ans, total)
        return ans