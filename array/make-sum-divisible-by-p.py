class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums) % p 
        if total == 0: 
            return 0
        prefix = {0: -1}
        cur = 0
        best_len = inf

        for i, num in enumerate(nums):
            cur = (cur + num) % p
            target = (cur - total) % p

            if target in prefix:
                best_len = min(best_len, i - prefix[target])

            prefix[cur] = i
        return best_len if best_len != inf else -1

            
            