class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = [False] * (n + 1)
        for num in nums:
            arr[num] = True
        result = []
        for i in range(1, n + 1):
            if arr[i] == False:
                result.append(i)
        return result

        