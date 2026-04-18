class Solution:
    def findLucky(self, arr: List[int]) -> int:
        ans = Counter(arr)
        max_ans = -1
        for k, v in ans.items():
            if k == v:
                max_ans = max(max_ans, k)
        return max_ans