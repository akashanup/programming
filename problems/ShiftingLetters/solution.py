class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        if len(s) == 0:
            return s
        shifts[-1] = shifts[-1] % 26
        # Calculate postfix sum
        for i in range(len(shifts) - 2, -1, -1):
            shifts[i] = (((shifts[i] % 26) + shifts[i + 1]) % 26)

        for i in range(len(shifts)):
            order = (ord(s[i]) - 96 + shifts[i]) % 26
            s = s[:i] + (chr(order + 96) if order > 0 else 'z') + s[i + 1:]
        return s
