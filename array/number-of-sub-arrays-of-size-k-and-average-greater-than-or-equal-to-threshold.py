class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)
        count = []
        window = sum(arr[:k]) / k
        if window >= threshold:
            count.append(window) 
            
        for right in range(k, n):
            window = (window * k + arr[right] - arr[right - k]) / k
            print(window)
            if window >= threshold:
                count.append(window)
        return len(count)