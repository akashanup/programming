class Solution:
    def dp(self, strs, m, n, idx, subsets, lookup):
        if m < 0 or n < 0:
            return -sys.maxsize
        if (m == 0 and n == 0) or idx == len(strs):
            return subsets
        key = (m, n, idx, subsets)
        if key not in lookup:
            lookup[key] = max(subsets, self.dp(strs, m-strs[idx].count("0"), n-strs[idx].count("1"), idx+1, subsets+1, lookup), self.dp(strs, m, n, idx+1, subsets, lookup))
        return lookup[key]

    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        return self.dp(strs, m, n, 0, 0, {})
