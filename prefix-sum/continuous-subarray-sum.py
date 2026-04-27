class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remaining_map = {0: -1}
        prefix = 0
        for i, num in enumerate(nums):
            prefix += num
            remaining = prefix % k

            if remaining in remaining_map:
                if i - remaining_map[remaining] >=2:
                    return True
            else:
                remaining_map[remaining] = i
        return False