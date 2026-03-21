class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        max_count = 0
        best_idx = -1
        for i, row in enumerate(mat):
            count = sum(row)
            if max_count < count:
                max_count = count
                best_idx = i
        return [best_idx, max_count]