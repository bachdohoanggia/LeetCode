class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)
        count = 0
        window = sum(arr[:k])
        if window / k >= threshold:
            count += 1 

        for right in range(k, n):
            window = window * k + arr[right] - arr[right - k]
            if window / k >= threshold:
                count += 1
        return count