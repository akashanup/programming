class Solution:
    def reverseWords(self, s: str) -> str:
        # Remove start and end spaces
        s = s.strip()

        # Remove more then one spaces in between words
        i = 1
        while i < len(s):
            if s[i] == ' ' and s[i-1] == ' ':
                s = s[:i] + s[i+1:]
            else:
                i += 1

        i = 0
        j = len(s) - 1
        start = 0
        end = len(s) - 1
        while start <= end:
            if s[start] == ' ' and s[end] == ' ':
                s = s[:i] + s[end+1:j+1] + s[start:end+1] + s[i:start] + s[j+1:]
                tempStart, tempEnd = start, end
                start = i + (j - tempEnd) + 1
                end = j - (tempStart - i) - 1
                i = start
                j = end
            if s[start] != ' ':
                start += 1
            if s[end] != ' ':
                end -= 1
        return s
