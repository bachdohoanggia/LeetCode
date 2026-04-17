class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_ct = Counter(chars)
        result = 0 
        for word in words:
            if Counter(word) - char_ct == Counter():
                result += len(word)
        return result