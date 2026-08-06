class Solution:
    def compare(self, str1, str2):
        return str1 + str2 < str2 + str1

    def smallestString(self, str):
        i = 1
        while i < len(str):
            key = str[i]
            j = i - 1
            while j >= 0 and self.compare(key, str[j]):
                str[j+1] = str[j]
                j -= 1
            str[j + 1] = key
            i += 1
        return ''.join(str)
