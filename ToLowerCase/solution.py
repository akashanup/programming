class Solution:
    def toLowerCase(self, s: str) -> str:
        lowerS = ''
        for ch in s:
            asciiOfCh = ord(ch)
            if asciiOfCh in range(65, 91):
                lowerS += chr(asciiOfCh + 32)
            else:
                lowerS += ch
        return lowerS
