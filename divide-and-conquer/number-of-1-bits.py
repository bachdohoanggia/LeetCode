class Solution:
    def hammingWeight(self, x: int) -> int:
        bin_x = bin(x)
        count = 0
        for digit in bin_x:
            if digit == "1":
                count += 1
        return count
        