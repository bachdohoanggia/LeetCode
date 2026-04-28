class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        prefix, result = 0, 0
        for num in nums:
            prefix += num
            result += count[prefix - goal]
            count[prefix] += 1
        return result
