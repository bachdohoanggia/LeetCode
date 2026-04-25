class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        min_value = 0
        for i in range(len(nums)):
            value = max(nums[:(i + 1)]) - min(nums[i:])
            if value <= k:
                return i
        return -1
            
            