class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left, right = 0, 0
        lvp = 0
        for ch in s:
            if ch == '(':
                left += 1
            else:
                right += 1

            if left == right:
                lvp = max(lvp, 2*right)
            elif right > left:
                left, right = 0, 0

        left, right = 0, 0
        for ch in s[::-1]:
            if ch == '(':
                left += 1
            else:
                right += 1

            if left == right:
                lvp = max(lvp, 2*left)
            elif left > right:
                left, right = 0, 0

        return lvp
