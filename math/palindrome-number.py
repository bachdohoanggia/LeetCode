class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        str_x = str(x)
        n = len(str_x)
        palindrome = ''
        for i in range(n - 1, -1, -1):
            palindrome += str_x[i]
        if int(palindrome) == x:
            return True
        return False

