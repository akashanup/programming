class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        lookup = {}
        for i in arr:
            if i in lookup:
                lookup[i] = lookup[i] + 1
            else:
                lookup[i] = 1
        lookupValues = lookup.values()
        lookupValues = sorted(lookupValues, reverse=True)
        arrLen = len(arr)
        maxLen = arrLen // 2
        count = 0
        for i in lookupValues:
            arrLen -= i
            count += 1
            if arrLen <= maxLen:
                break
        return count
