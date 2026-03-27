class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        max_count = -inf
        idx = -1
        for i, matrix in enumerate(mat):
            count = sum(matrix)
            if max_count < count:
                max_count = count
                idx = i
            return (idx, max_count)