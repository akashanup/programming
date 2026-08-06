class Solution:
    def dp(self, hashmap, ch, n, lookup):
        if n == 0:
            return 1
        if (ch, n) not in lookup:
            count = 0
            for c in hashmap[ch]:
                count += self.dp(hashmap, c, n-1, lookup)
            lookup[(ch, n)] = count % ((10**9) + 7)
        return lookup[(ch, n)]

    def countVowelPermutation(self, n: int) -> int:
        hashmap = {
            '': ('a', 'e', 'i', 'o', 'u'),
            'a': ('e'),
            'e': ('a', 'i'),
            'i': ('a', 'e', 'o', 'u'),
            'o': ('i', 'u'),
            'u': ('a'),
        }
        return self.dp(hashmap, '', n, {})