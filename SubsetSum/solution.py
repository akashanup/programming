class Solution:
    def dp(self, arr, target, index, lookup, subset):
        if target == 0:
            return [subset]
        if index == len(arr) or target < 0:
            return []
        key = index, target
        if key not in lookup:
            lookup[key] = self.dp(arr, target-arr[index], index+1, lookup, subset+[arr[index]]) + self.dp(arr, target, index+1, lookup, subset)
            """
                If only one subset is required.
                ans = self.dp(arr, target-arr[index], index+1, lookup, subset+[arr[index]])
                if not ans:
                    ans = self.dp(arr, target, index+1, lookup, subset)
                lookup[key] = ans
            """
        return lookup[key]

    def subsetSum(self, arr, target):
        return self.dp(arr, target, 0, {}, [])


print(Solution().subsetSum([15, 22, 14, 26, 32, 9, 16, 8], 53))
print(Solution().subsetSum([12, 1, 61, 5, 9, 2], 24))
