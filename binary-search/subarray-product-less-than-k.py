class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        left = 0
        product = 1

        if k == 0:
            return 0
            
        for right in range(n):
            product *= nums[right]
            while product >= k:
                product = product // nums[left]
                left += 1
            ans += right - left + 1 
        return ans