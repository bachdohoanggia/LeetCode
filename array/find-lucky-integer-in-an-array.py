class Solution:
    def findLucky(self, arr: List[int]) -> int:
        ans = Counter(arr)
        max_ans = -1
        for k, v in ans.items():
            if k == v and k > max_ans:
                max_ans = k
        return max_ans
    