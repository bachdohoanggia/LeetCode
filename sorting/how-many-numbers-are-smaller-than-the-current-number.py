class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_num = sorted(nums)
        for i in range(len(nums)):
            nums[i] = sorted_num.index(nums[i])
        return nums