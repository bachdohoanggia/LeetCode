class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = [0] * (n + 1)
        for num in nums:
            arr[num] = 1
        result = []
        for i in range(1, n + 1):
            if arr[i] == 0:
                result.append(i)
        return result

        