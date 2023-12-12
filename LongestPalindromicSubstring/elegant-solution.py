class Solution:
    def checkPalindrome(self, s, backward, forward):
        while backward >= 0 and forward < len(s) and s[backward] == s[forward]:
            backward -= 1
            forward += 1
        return s[backward + 1: forward]

    def longestPalindrome(self, s: str) -> str:
        longest = ""
        for i in range(len(s)):
            # Make ith element as the middle element of odd length palindrome string.
            # Keep moving backward and forward as long as the resulting string is palindrome.
            oddPalindromes = self.checkPalindrome(s, i, i)
            # Make ith and (i+1)th element as the middle elements of even length palindrome string.
            # Keep moving backward and forward as long as the resulting string is palindrome.
            evenPalindromes = self.checkPalindrome(s, i, i + 1)
            if len(oddPalindromes) > len(evenPalindromes):
                if len(oddPalindromes) > len(longest):
                    longest = oddPalindromes
            else:
                if len(evenPalindromes) > len(longest):
                    longest = evenPalindromes

        return longest
