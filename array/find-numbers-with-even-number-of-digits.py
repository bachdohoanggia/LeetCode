class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0 
        for num in nums:
            strnum = str(num)
            if len(strnum) % 2 == 0:
                count += 1
        return count
