class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        n = len(nums)
        if n < k:
            return 0

        count = defaultdict(int)
        window = 0

        for i in range(k):
            count[nums[i]] += 1
            window += nums[i]
        max_sum = window if len(count) >= m else 0

        for right in range(k, n):
            window = window + nums[right] - nums[right - k]
            count[nums[right]] += 1
            count[nums[right - k]] -= 1
            
            if count[nums[right - k]] == 0:
                del count[nums[right - k]]

            if len(count) >= m:
                max_sum = max(max_sum, window)
        return max_sum

            
