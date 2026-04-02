class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = {}
        n = len(nums)
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        for num in nums:
            if freq[num] != 2:
                return num