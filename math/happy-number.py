class Solution:
    def isHappy(self, n: int) -> bool:
        freq = {}
        while n != 1:
            if n in freq:
                return False
            freq[n] = 1
            total = 0
            for ch in str(n):
                total += int(ch) ** 2
            n = total

        return True


            