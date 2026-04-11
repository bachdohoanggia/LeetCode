class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        set1 = set('qwertyuiop')
        set2 = set('asdfghjkl')
        set3 = set('zxcvbnm')
        sets = [set1, set2, set3]
        result = []
        for s in sets:
            for word in words :
                valid_word = True
                for ch in word.lower():
                    if ch not in s:
                        valid_word = False
                if valid_word == True:
                    result.append(word)
        return result
                        