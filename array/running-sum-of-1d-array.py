class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        arr = [0]*len(nums)
        for i in range(len(nums)):
            if i == 0:
                arr[i] = nums[i]
            else:
                arr[i] = nums[i] + arr[i - 1]
        return arr
