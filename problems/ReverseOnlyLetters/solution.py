class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        start = 0
        end = len(s) - 1
        alphabets = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]
        while start < end:
            while start < end and s[start] not in alphabets:
                start += 1
            while start < end and s[end] not in alphabets:
                end -= 1
            if s[start] in alphabets and s[end] in alphabets:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
        return ''.join(s)
