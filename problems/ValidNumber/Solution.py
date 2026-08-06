class Solution:
    def isNumber(self, s: str) -> bool:
        invalidChars = [chr(x) for x in range(ord('a'), ord('z') + 1) if chr(x) != 'e'] + [chr(x) for x in range(ord('A'), ord('Z') + 1) if chr(x) != 'E']
        digits = [str(digit) for digit in range(10)]

        digitCount = 0
        for digit in s:
            if digit in digits:
                digitCount += 1
        if digitCount == 0:
            return False

        for invalidChar in invalidChars:
            if invalidChar in s:
                return False

        if s.count('e') > 1 or s.count('E') > 1 or s.count('+') > 2 or s.count('-') > 2 or s.count('.') > 1:
            return False

        indexOfE = None
        if 'e' in s or 'E' in s:
            indexOfE = s.index('e') if 'e' in s else s.index('E')
        if indexOfE is not None and (indexOfE == 0 or indexOfE == (len(s) - 1) or (s[indexOfE - 1] not in digits and s[indexOfE - 1] != ".")):
            return False

        indexOfDecimal = None
        if '.' in s:
            indexOfDecimal = s.index('.')
        if indexOfDecimal is not None and ((indexOfE is not None and indexOfDecimal > indexOfE) or (indexOfDecimal == 0 and indexOfDecimal == (len(s) - 1))):
            return False

        indexOfDecimalAndE = None
        if ".E" in s or ".e" in s:
            indexOfDecimalAndE = s.index('.E') if '.E' in s else s.index('.e')
        if indexOfDecimalAndE is not None and (indexOfDecimalAndE == 0 or s[indexOfDecimalAndE - 1] not in digits):
            return False

        lastIndexOfPlus = lastIndexOfMinus = None
        if '+' in s[1:]:
            lastIndexOfPlus = s.index('+', 1)
        if '-' in s[1:]:
            lastIndexOfMinus = s.index('-', 1)
        if (lastIndexOfPlus and (s[lastIndexOfPlus - 1] not in ['e', 'E'] or lastIndexOfPlus == len(s) -1)) or (lastIndexOfMinus and s[lastIndexOfMinus - 1] not in ['e', 'E'] or lastIndexOfMinus == len(s) -1):
            return False
        return True
