class Solution:
    def constructAlignment2(self, a, b, dp, i, j, alignment):
        if i == j == 0:
            return
        if i > 0 and dp[i][j] == dp[i - 1][j]:
            # Deletion
            self.constructAlignment2(a, b, dp, i - 1, j, alignment)
            alignment[0].append(a[i - 1])
            alignment[1].append('-')
        elif j > 0 and dp[i][j] == dp[i][j - 1]:
            # Insertion
            self.constructAlignment2(a, b, dp, i, j - 1, alignment)
            alignment[0].append('-')
            alignment[1].append(b[j - 1])
        else:
            # Match - Mismatch
            self.constructAlignment2(a, b, dp, i - 1, j - 1, alignment)
            alignment[0].append(a[i - 1])
            alignment[1].append(b[j - 1])

    def constructAlignment1(self, a, b, dp, i, j, alignment):
        if i == j == 0:
            return
        if j > 0 and dp[i][j] == dp[i][j - 1]:
            # Insertion
            self.constructAlignment1(a, b, dp, i, j - 1, alignment)
            alignment[0].append('-')
            alignment[1].append(b[j - 1])
        elif i > 0 and dp[i][j] == dp[i - 1][j]:
            # Deletion
            self.constructAlignment1(a, b, dp, i - 1, j, alignment)
            alignment[0].append(a[i - 1])
            alignment[1].append('-')
        else:
            # Match - Mismatch
            self.constructAlignment1(a, b, dp, i - 1, j - 1, alignment)
            alignment[0].append(a[i - 1])
            alignment[1].append(b[j - 1])

    def lcs3(self, a, b, c):
        lenA = len(a)
        lenB = len(b)
        lenC = len(c)
        dp = [[0 for i in range(lenB + 1)] for j in range(lenA + 1)]
        for i in range(1, lenA + 1):
            for j in range(1, lenB + 1):
                insertion = dp[i][j - 1]
                deletion = dp[i - 1][j]
                match = dp[i - 1][j - 1] + 1
                mismatch = dp[i - 1][j - 1]
                if a[i - 1] == b[j - 1]:
                    dp[i][j] = max(insertion, deletion, match)
                else:
                    dp[i][j] = max(insertion, deletion, mismatch)
        # Construct the optimal alignment
        alignment = [[], []]
        self.constructAlignment1(a, b, dp, lenA, lenB, alignment)
        ab = [alignment[0][i] for i in range(len(alignment[0])) if alignment[0][i] == alignment[1][i]]
        lenAB1 = len(ab)
        dp1 = [[0 for i in range(lenAB1 + 1)] for j in range(lenC + 1)]
        for i in range(1, lenC + 1):
            for j in range(1, lenAB1 + 1):
                insertion = dp1[i][j - 1]
                deletion = dp1[i - 1][j]
                match = dp1[i - 1][j - 1] + 1
                mismatch = dp1[i - 1][j - 1]
                if c[i - 1] == ab[j - 1]:
                    dp1[i][j] = max(insertion, deletion, match)
                else:
                    dp1[i][j] = max(insertion, deletion, mismatch)
        # Construct the other optimal alignment (if possible)
        alignment = [[], []]
        self.constructAlignment2(a, b, dp, lenA, lenB, alignment)
        ab = [alignment[0][i] for i in range(len(alignment[0])) if alignment[0][i] == alignment[1][i]]
        lenAB2 = len(ab)
        dp2 = [[0 for i in range(lenAB2 + 1)] for j in range(lenC + 1)]
        for i in range(1, lenC + 1):
            for j in range(1, lenAB2 + 1):
                insertion = dp2[i][j - 1]
                deletion = dp2[i - 1][j]
                match = dp2[i - 1][j - 1] + 1
                mismatch = dp2[i - 1][j - 1]
                if c[i - 1] == ab[j - 1]:
                    dp2[i][j] = max(insertion, deletion, match)
                else:
                    dp2[i][j] = max(insertion, deletion, mismatch)
        return max(dp1[lenC][lenAB1], dp2[lenC][lenAB2])
