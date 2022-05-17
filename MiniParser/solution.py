# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
    def __init__(self, value=None):
        """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """

    def isInteger(self):
        """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

    def add(self, elem):
        """
       Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
       :rtype void
       """

    def setInteger(self, value):
        """
       Set this NestedInteger to hold a single integer equal to value.
       :rtype void
       """

    def getInteger(self):
        """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """

    def getList(self):
        """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """


class Solution:
    def parseNumber(self, s, idx, isNegative=False):
        num = 0
        while idx < len(s) and s[idx].isdigit():
            num = num * 10 + int(s[idx])
            idx += 1
        if isNegative:
            num = -num
        return NestedInteger(num), idx

    def parseList(self, s, idx):
        obj = NestedInteger()
        while idx < len(s) and s[idx] != ']':
            if s[idx].isdigit():
                data, idx = self.parseNumber(s, idx)
                obj.add(data)
            elif s[idx] == '-':
                data, idx = self.parseNumber(s, idx + 1, True)
                obj.add(data)
            elif s[idx] == '[':
                data, idx = self.parseList(s, idx + 1)
                obj.add(data)
            else:
                idx += 1

        return obj, idx + 1

    def deserialize(self, s: str) -> NestedInteger:
        if s[0] != '[':
            if s[0] == '-':
                nestedInteger, _ = self.parseNumber(s, 1, True)
            else:
                nestedInteger, _ = self.parseNumber(s, 0)
            return nestedInteger

        nestedInteger = NestedInteger()

        i = 1
        while i < len(s):
            if s[i].isdigit():
                data, i = self.parseNumber(s, i)
                nestedInteger.add(data)
            if s[i] == '-':
                data, i = self.parseNumber(s, i + 1, True)
                nestedInteger.add(data)
            elif s[i] == '[':
                data, i = self.parseList(s, i + 1)
                nestedInteger.add(data)
            else:
                i += 1

        return nestedInteger
