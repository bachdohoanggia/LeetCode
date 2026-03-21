class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = [0] * len(indices)
        for letter, index in zip(s, indices):
            ans[index] = letter
        return "".join(ans)
