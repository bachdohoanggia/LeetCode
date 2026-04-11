from typing import List

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # Khởi tạo với từ đầu tiên
        freq = {}
        for char in words[0]:
            freq[char] = freq.get(char, 0) + 1
        
        # Với mỗi từ tiếp theo
        for word in words[1:]:

            # Đếm tần suất của từ hiện tại
            word_freq = {}
            for char in word:
                word_freq[char] = word_freq.get(char, 0) + 1
            
            # Cập nhật freq = min(freq, word_freq)
            for char in freq:
                freq[char] = min(freq[char], word_freq.get(char, 0))
            
        result = []
        # Chuyển thành kết quả
        for char, count in freq.items():
            if count > 0:
                result.extend([char] * count)
        return result
        
        
        return result