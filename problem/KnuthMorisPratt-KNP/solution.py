class KNP:
    def lpsArray(self, pat):
        n = len(pat)
        lps = [0] * n
        i = 1
        longestPrefixLen = 0  # Length of previous longest prefix
        while i < n:
            if pat[i] == pat[longestPrefixLen]:
                longestPrefixLen += 1
                lps[i] = longestPrefixLen
                i += 1
            else:
                if longestPrefixLen > 0:
                    longestPrefixLen = lps[longestPrefixLen - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    def search(self, txt, pat):
        m = len(txt)
        n = len(pat)
        lps = self.lpsArray(pat)
        print(lps)
        i = 0
        j = 0
        while i < m:
            if txt[i] == pat[j]:
                i += 1
                j += 1
            if j == n:
                print("Pattern found at index", i - j)
                j = lps[j - 1]
            elif txt[i] != pat[j] and i < m:  # Mismatch after j matches
                # Do not match lps[0..lps[j-1]] characters, they will match anyway
                if j > 0:
                    j = lps[j - 1]
                else:
                    i += 1


print(KNP().search(txt="ABABDABACDABABCABAB", pat="ABABCABAB"))
print(KNP().search(txt="AABAACAADAABAABA", pat="AABA"))
print(KNP().search(txt="ABCDEFGH", pat="BCDE"))

