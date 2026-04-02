class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq = {}
        for char in s:
            if char not in s_freq:
                s_freq[char] = 0
            s_freq[char] = +1
        t_freq = {}
        for char in t:
            if char not in t_freq:
                t_freq[char] = 0
            t_freq[char] = +1
        return s_freq == t_freq