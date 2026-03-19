class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        arr = []  
        for num, idx in zip(nums, index):
            arr.insert(idx, num)
        return arr
    