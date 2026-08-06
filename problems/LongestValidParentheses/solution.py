"""
Logic:
    This problem can be solved by using Dynamic Programming. We make use of a \text{dp}dp array where iith element of \text{dp}dp represents the length of the longest valid substring ending at iith index. We initialize the complete \text{dp}dp array with 0's. Now, it's obvious that the valid substrings must end with \text{‘)’}‘)’. This further leads to the conclusion that the substrings ending with \text{‘(’}‘(’ will always contain '0' at their corresponding \text{dp}dp indices. Thus, we update the \text{dp}dp array only when \text{‘)’}‘)’ is encountered.
    To fill dp array we will check every two consecutive characters of the string and if:
        1. s[i] == ‘)’ and s[i−1] == ‘(’, i.e. string looks like ``.......()"⇒
            dp[i] = dp[i-2] + 2
            We do so because the ending "()" portion is a valid substring anyhow and leads to an increment of 2 in the length of the just previous valid substring's length.

        2. s[i] == ‘)’ and s[i−1] ==‘)’, i.e. string looks like ``.......))" ⇒
            if s[i−dp[i−1]−1]=‘(’ then
                dp[i] = dp[i−1] + dp[i−dp[i−1]−2] + 2
                We do so because we have to accommodate the last ')'
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        lvp = 0

        dp = [0] * len(s)
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i-1] == '(':
                    dp[i] = 2 + (dp[i-2] if i > 1 else 0)
                elif i-dp[i-1]-1 >= 0 and s[i-dp[i-1]-1] == '(':
                    dp[i] = 2 + dp[i-1] + (dp[i-dp[i-1]-2] if i-dp[i-1]-2 >= 0 else 0)
                lvp = max(lvp, dp[i])

        return lvp
