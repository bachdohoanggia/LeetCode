class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortnums = sorted(nums)
        for i in range(len(nums)):
            nums[i] = sortnums.index(nums[i])
        return nums
