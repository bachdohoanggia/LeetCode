class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        n = len(arr)
        ans = []
        for i in range(n):
                if arr[i]/2 not in ans and arr[i]*2 not in ans:
                    ans.append(arr[i])
                else:
                    return True
        return False
                