class Solution:
    def dpFn(self, s, i, lookup):
        if i < 0:
            return 1
        if lookup[i] is not None:
            return lookup[i]
        if s[i] == "*":
            decoding = (9 * self.dpFn(s, i - 1, lookup)) % ((10 ** 9) + 7)
            if i > 0:
                if s[i - 1] == "1":
                    decoding = (decoding + (9 * self.dpFn(s, i - 2, lookup))) % ((10 ** 9) + 7)
                elif s[i - 1] == "2":
                    decoding = (decoding + (6 * self.dpFn(s, i - 2, lookup))) % ((10 ** 9) + 7)
                elif s[i - 1] == "*":
                    decoding = (decoding + (15 * self.dpFn(s, i - 2, lookup))) % ((10 ** 9) + 7)
            lookup[i] = decoding
            return lookup[i]
        if s[i] != "0":
            decoding = self.dpFn(s, i - 1, lookup)
        else:
            decoding = 0
        if i > 0:
            if s[i - 1] == "1":
                decoding = (decoding + self.dpFn(s, i - 2, lookup)) % ((10 ** 9) + 7)
            elif s[i - 1] == "2" and s[i] <= "6":
                decoding = (decoding + self.dpFn(s, i - 2, lookup)) % ((10 ** 9) + 7)
            elif s[i - 1] == "*":
                decoding = (decoding + ((2 if s[i] <= "6" else 1) * self.dpFn(s, i - 2, lookup))) % ((10 ** 9) + 7)
        lookup[i] = decoding
        return lookup[i]

    def numDecodings(self, s: str) -> int:
        n = len(s)
        lookup = [None] * n
        return self.dpFn(s, n - 1, lookup)


print(Solution().numDecodings("11106"))
print(Solution().numDecodings("1116"))
print(Solution().numDecodings("1*"))
print(Solution().numDecodings("2*"))
print(Solution().numDecodings("*"))
print(Solution().numDecodings("7*9*3*6*3*0*5*4*9*7*3*7*1*8*3*2*0*0*6*"))
