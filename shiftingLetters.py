class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        cumulative_shifts = [0] * (n + 1)

        # Calculate the cumulative shifts in reverse order
        for start, end, direction in shifts:
            shift_direction = 1 if direction == 1 else -1
            cumulative_shifts[start] += shift_direction
            cumulative_shifts[end + 1] -= shift_direction

        result = []
        for i in range(n):
            if i != 0:
                cumulative_shifts[i] += cumulative_shifts[i - 1]
            new_chr_ascii = (ord(s[i]) - ord("a") + cumulative_shifts[i]) % 26 + ord("a")
            result.append(chr(new_chr_ascii))

        return ''.join(result)