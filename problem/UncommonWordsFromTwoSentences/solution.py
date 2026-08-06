"""
# Intuition
An uncommon word is a word that appears exactly once in one sentence and does not appear in the other sentence.  
To efficiently find such words, we can count the frequency of every word from both sentences together.  
Any word with frequency `1` will be part of the answer.

# Approach
1. Split both sentences into individual words.
2. Use a hash map (`wordsCount`) to store the frequency of each word.
3. Traverse through the frequency map.
4. Add all words with frequency `1` to the result list.
5. Return the result.

This works because:
- common words will appear more than once,
- repeated words inside the same sentence will also have frequency greater than `1`.

# Complexity
- Time complexity: $$O(n + m)$$
Where:
    - `n` = number of words in `s1`
    - `m` = number of words in `s2`

- Space complexity: $$O(n + m)$$
"""

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        wordsCount = {}
        s = s1.split(" ")
        s += s2.split(" ")
        for word in s:
            if word not in wordsCount:
                wordsCount[word] = 0
            wordsCount[word] += 1
        
        uncommonWords = []
        for word,count in wordsCount.items():
            if count == 1:
                uncommonWords.append(word)
        
        return uncommonWords
