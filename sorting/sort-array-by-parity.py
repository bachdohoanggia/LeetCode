class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        evenli = []
        oddli = []
        for num in nums:
            if num % 2 == 0:
                evenli.append(num)
            else:
                oddli.append(num)
        return evenli + oddli