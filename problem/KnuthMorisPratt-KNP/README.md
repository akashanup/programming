# Knuth Moris Pratt - Pattern Searching Algorithm

The worst case complexity of the Naive algorithm is O(m(n-m+1)). So we needed a better approach to search a pattern.
Therefore, we use KNP algorithm because, The time complexity of KMP algorithm is O(n) in the worst case.

The Naive pattern searching algorithm does not work well in cases where we see many matching characters followed by a mismatching character.

The KMP matching algorithm uses degenerating property (pattern having same sub-patterns appearing more than once in the pattern) of the pattern and improves the worst case complexity to O(n). The basic idea behind KMP’s algorithm is: whenever we detect a mismatch (after some matches), we already know some of the characters in the text of the next window. We take advantage of this information to avoid matching the characters that we know will anyway match.
- An important question arises from the above explanation, 
how to know how many characters to be skipped. To know this, 
we pre-process pattern and prepare an integer array 
lps[] that tells us the count of characters to be skipped. 

**Searching Algorithm:**

Unlike Naive algorithm, where we slide the pattern by one and compare all characters at each shift, we use a value from lps[] to decide the next characters to be matched. The idea is to not match a character that we know will anyway match.

How to use lps[] to decide next positions (or to know a number of characters to be skipped)?

- We start comparison of pat[j] with j = 0 with characters of current window of text.
- We keep matching characters txt[i] and pat[j] and keep incrementing i and j while pat[j] and txt[i] keep matching.
- When we see a mismatch
- We know that characters pat[0..j-1] match with txt[i-j…i-1] (Note that j starts with 0 and increment it only when there is a match).
- We also know (from above definition) that lps[j-1] is count of characters of pat[0…j-1] that are both proper prefix and suffix.
- From above two points, we can conclude that we do not need to match these lps[j-1] characters with txt[i-j…i-1] because we know that these characters will anyway match.
