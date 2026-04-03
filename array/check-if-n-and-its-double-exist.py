class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        n = len(arr)
        for i in range(n):
                if arr[i]/2 in arr or arr[i]*2 in arr:
                    return True
        return False
                