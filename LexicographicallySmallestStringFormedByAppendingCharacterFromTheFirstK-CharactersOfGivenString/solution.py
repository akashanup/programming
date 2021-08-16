class Solution:
    def smallestString(self, str, k):
        result = ''
        while str:
            smallest = 0
            i = 1
            while i < k and i < len(str):
                if str[smallest] >= str[i]:
                    smallest = i
                i += 1
            result += str[smallest]
            str = str[:smallest] + str[smallest + 1:]
        return result
