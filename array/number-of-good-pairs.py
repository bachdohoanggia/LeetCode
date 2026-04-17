class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq = Counter(nums)
        result = 0
        for count in freq.values():
            result += count * (count - 1) // 2
        return result
