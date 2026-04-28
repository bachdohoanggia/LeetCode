class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        prefix = [0] * n
        prefix[0] = nums[0]
        count = 0
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + nums[i]
        for i in range(n):
            for j in range(i, n):
                if i == 0:
                    total = prefix[j]
                else:
                    total = prefix[j] - prefix[i-1]
                if total == goal:
                    count += 1
        return count
