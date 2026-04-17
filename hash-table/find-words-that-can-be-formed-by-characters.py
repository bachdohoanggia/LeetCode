class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        result = 0 
        for word in words:
            if Counter(word) - Counter(chars) == Counter():
                result += len(word)
        return result