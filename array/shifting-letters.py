class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        n = len(s)
        prefix = list(accumulate(shifts))
        total = prefix[-1]
        

        result = []
        for i in range(n):
            if i == 0:
                shift_amount = total % 26
            else:
                shift_amount = (total - prefix[i - 1]) % 26
            new_char = chr((ord(s[i]) - ord("a") + shift_amount) % 26 + ord("a"))
            result.append(new_char)
            
        return "".join(result)