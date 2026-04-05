class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        for num in arr:
            if num/2 not in seen and num*2 not in seen:
                seen.add(num)
            else:
                return True
        return False
                