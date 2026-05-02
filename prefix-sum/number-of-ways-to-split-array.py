class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix = list(accumulate(nums))
        count = 0
        total = prefix[-1]
        for i in range(len(nums) - 1):
            if prefix[i] >= total - prefix[i]:
                count += 1
        return count
            