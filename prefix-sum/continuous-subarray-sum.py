class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remaining_map = {0: -1}
        prefix_sum = 0
        for i, num in enumerate(nums):
            prefix_sum += num
            remaining = prefix_sum % k

            if remaining in remaining_map:
                if i - remaining_map[remaining] >= 2:
                    return True
            else:
                remaining_map[remaining] = i
        return False
