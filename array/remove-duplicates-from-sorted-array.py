class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for i in range(len(nums)):
            if i == 0:
                nums[k] = nums[i]
            elif i > 0:
                if nums[i] != nums[k]:
                    nums[k + 1] = nums[i]
                    k += 1
        return k + 1
