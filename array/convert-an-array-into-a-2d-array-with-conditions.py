class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        freq = Counter(nums)
        max_freq = max(freq.values())
        arr = [[] for _ in range(max_freq)]
        for num, count in freq.items():
            for i in range(count):
                arr[i].append(num)
        return arr