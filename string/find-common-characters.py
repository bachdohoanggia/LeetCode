from typing import List

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # Khởi tạo với từ đầu tiên
        freq = Counter(words[0])
        
        # Với mỗi từ tiếp theo
        for word in words[1:]:

            # Đếm tần suất của từ hiện tại
            word_freq = Counter(word)
            
            # Cập nhật freq = min(freq, word_freq)
            for char, f in freq.items():
                freq[char] = min(f, word_freq.get(char, 0))
            
        return list(freq.elements())
        