class Solution:
    def countLargestGroup(self, n: int) -> int:
        groups = Counter()
        for num in range(1, n+1):
            digit_sum = sum(int(d) for d in str(num))
            groups[digit_sum] += 1
        
        max_size = max(groups.values())

        count = 0
        for group in groups.values():
            if group == max_size:
                count += 1
        return count