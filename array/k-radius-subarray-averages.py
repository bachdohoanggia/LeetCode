class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        avg = [-1] * n
        max_sum = 0
        for i in range(n):
            if i - k < 0 or i + k >= n:
                avg[i] = -1
            else:
                avg[i] = sum(nums[i-k : i+k+1]) // (2*k+1)
                
        return avg
