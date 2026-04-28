class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        min_idx = 0
        prefix = [0] * n
        prefix[0] = nums[0]
        res = []
        total = sum(nums)
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + nums[i]
            
        for i in range(n):
            ans = abs(prefix[i]//(i + 1) - ((total - prefix[i])//(n - i - 1) if i < n - 1 else 0))
            res.append(ans)
            
        for i in range(1, n):
            if res[i] <= res[min_idx]:
                min_idx = i
        return min_idx
                



        