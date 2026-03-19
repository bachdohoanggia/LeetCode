class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        leftSum = [0] * n
        rightSum = [0] * n
        ans = [0] * n
        for i in range(n):
            leftSum[i] = sum(nums[:i])
            rightSum[i] = sum(nums[i + 1:])
            ans[i] = abs(leftSum[i] - rightSum[i])
        return ans