class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        i, j = len(S) - 1, len(T) - 1
        backspaceS = backspaceT = 0
        # Start iterating from right to left for both the strings.
        while True:
            # If the ith char in S is a # or there are remaining backspaces that have not been used yet, decrease the value of i and update backspaces. Once this while loop terminates, the char at ith position denotes that this char is actual part of final S.
            while i >= 0 and (backspaceS or S[i] == '#'):
                backspaceS += 1 if S[i] == '#' else -1
                i -= 1
            # If the ith char in S is a # or there are remaining backspaces that have not been used yet, decrease the value of i and update backspaces. Once this while loop terminates, the char at ith position denotes that this char is actual part of final T.
            while j >= 0 and (backspaceT or T[j] == '#'):
                backspaceT += 1 if T[j] == '#' else -1
                j -= 1
            # If at anytime S[i] doesn't match with S[j], we can say that the two strings starts to differ from this position when moving from right to left.
            # Or if we have processed the entire strings(i== -1 and j == -1) then we may conclude that both the strings are same.
            if not (i >= 0 and j >= 0 and S[i] == T[j]):
                return i == j == -1
            i, j = i - 1, j - 1
