class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        n = len(arr)
        if n == 2:
            return True
        arr.sort()
        for i in range(n - 2):
            if abs(arr[i] - arr[i + 1]) == abs(arr[i + 1] - arr[i + 2]):
                return True
        return False
