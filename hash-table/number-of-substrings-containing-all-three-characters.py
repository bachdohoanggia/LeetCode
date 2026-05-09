class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        left = 0
        count = defaultdict(int)

        for right in range(n):
            count[s[right]] += 1

            while len(count) == 3:
                count[s[left]] -= 1
                if count[s[left]] == 0:
                    del count[s[left]]
                left += 1
            ans += left
        return ans