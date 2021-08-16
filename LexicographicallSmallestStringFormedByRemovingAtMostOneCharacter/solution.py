class Solution:
    def smallestString(self, str):
        i = 0
        while i < len(str) - 1:
            if str[i] > str[i + 1]:
                break
            i += 1
        return str[:i] + str[i+1:]
