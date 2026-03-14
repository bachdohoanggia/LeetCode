class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums: 
            count += 1 if (len(str(num)) % 2 == 0) else 0
        return count
