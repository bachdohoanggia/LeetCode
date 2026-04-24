class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        n = len(s)
        total = sum(shifts)
        prefix = [0] * n
        prefix[0] = shifts[0]

        for i in range(1, n):
            prefix[i] = prefix[i - 1] + shifts[i]

        result = []
        for i in range(n):
            if i == 0:
                shift_amount = total % 26
            else:
                shift_amount = (total - prefix[i - 1]) % 26
            new_char = chr((ord(s[i]) - ord("a") + shift_amount) % 26 + ord("a"))
            result.append(new_char)
            
        return "".join(result)