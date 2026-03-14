class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        onecount = 0
        ans = 0
        for num in nums:
            if num == 1:
                onecount += 1
            else:
                onecount = 0
            ans = max(onecount, ans)
        return ans
