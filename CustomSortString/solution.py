class Solution:
    def customSortString(self, order: str, str: str) -> str:
        for i in order[::-1]:
            if i in str:
                count = str.count(i)
                str = str.replace(i, '')
                str = (i * count) + str
        return str
