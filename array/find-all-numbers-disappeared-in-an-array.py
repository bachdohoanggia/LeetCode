class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        appear = [0] * (n + 1)
        for num in nums:
            appear[num] = 1
            
        ans = []
        for i in range(1, n + 1):
            if appear[i] == 0:
                ans.append(i)
        return ans