class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        diff1 = []
        diff2 = []
        for num1 in nums1:
            if num1 not in nums2 and num1 not in diff1:
                diff1.append(num1)
        for num2 in nums2:
            if num2 not in nums1 and num2 not in diff2:
                diff2.append(num2)
        return [diff1, diff2]