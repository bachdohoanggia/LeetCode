class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        p_to_s = {}
        s_to_p = {}

        for ch, word in zip(pattern, words):
            if ch in p_to_s:
                if p_to_s[ch] != word:
                    return False
            else:
                if word in s_to_p:
                    return False
                p_to_s[ch] = word
                s_to_p[word] = ch
        return True
        