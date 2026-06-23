class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        freq = Counter(words[0])
        for word in words[1:]:

            word_freq = Counter(word)
            
            for ch, f in freq.items():
                freq[ch] = min(f, word_freq.get(ch,0))
            
        return list(freq.elements())
        