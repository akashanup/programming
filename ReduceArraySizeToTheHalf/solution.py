class Solution:
    def minSetSize(self, arr):
        lookup = {}
        for i in arr:
            if i in lookup:
                lookup[i] = lookup[i] + 1
            else:
                lookup[i] = 1
        # print(lookup)
        lookupValues = lookup.values()
        lookupValues = sorted(lookupValues, reverse=True)
        # print(lookupValues)
        arrLen = len(arr)
        maxLen = arrLen // 2
        count = 0
        for i in lookupValues:
            arrLen -= i
            count += 1
            if arrLen <= maxLen:
                break
        return count


print(Solution().minSetSize([3, 3, 3, 3, 5, 5, 5, 2, 2, 7]))
print(Solution().minSetSize([7, 7, 7, 7, 7, 7]))
print(Solution().minSetSize([1, 9]))
print(Solution().minSetSize([1000, 1000, 3, 7]))
print(Solution().minSetSize([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
