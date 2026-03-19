class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        evenarr = []
        oddarr = []
        for num in nums:
            if num % 2 == 0:
                evenarr.append(num)
            else:
                oddarr.append(num)
        return (evenarr + oddarr)
        