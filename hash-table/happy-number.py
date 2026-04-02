class Solution:
    def isHappy(self, n: int) -> bool:
        freq = {}  
        while n != 1:
            if n in freq:
                return False
                
            freq[n] = 1
            tong = 0
            for d in str(n):
                tong += int(d) ** 2
            n = tong
        
        return True 