class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix_odd = defaultdict(int, {0: 1})
        curr_odd = 0
        valid = 0
        for num in nums:
            curr_odd += num % 2
            prefix_odd[curr_odd] += 1
            valid += prefix_odd[curr_odd - k]
        return valid