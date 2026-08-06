class Solution:
    def optimal(self, a, b, target):
        a.sort(key=lambda x: x[1])
        b.sort(key=lambda x: x[1], reverse=True)
        iA = 0
        iB = 0
        lookup = {}
        optimal = None
        while iA < len(a) and iB < len(b):
            temp = a[iA][1] + b[iB][1]
            if temp <= target:
                if optimal is None:
                    optimal = temp
                else:
                    optimal = max(optimal, temp)
                if temp in lookup:
                    lookup[temp].append([a[iA][0], b[iB][0]])
                else:
                    lookup[temp] = [[a[iA][0], b[iB][0]]]
            if a[iA][1] + b[iB][1] == target:
                iA += 1
                iB += 1
            elif a[iA][1] + b[iB][1] > target:
                iB += 1
            else:
                iA += 1
        return lookup[optimal] if optimal else []


a = [[1, 3], [2, 5], [3, 7], [4, 10]]
b = [[1, 2], [2, 3], [3, 4], [4, 5]]
target = 10
a = [[1, 8], [2, 7], [3, 14]]
b = [[1, 5], [2, 10], [3, 14]]
target = 20
a = [[1, 2], [2, 4], [3, 6]]
b = [[1, 2]]
target = 7
print(Solution().optimal(a, b, target))
