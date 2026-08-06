"""
# Intuition
The first character of a word determines which keyboard row the entire word must belong to.
So, after identifying the row of the first character, we only need to verify whether all remaining characters belong to the same row.

# Approach
- Store all three keyboard rows using sets for fast lookup.
- Convert each word to lowercase to handle case insensitivity.
- Determine the row using the first character of the word.
- Check if every remaining character belongs to the same row using a helper function.
- If valid, add the word to the answer list.

# Complexity
- Time complexity: $$O(n⋅m)$$

Where:

n = number of words

m = maximum length of a word

- Space complexity: $$O(1)$$. Only constant extra space is used for the keyboard row sets.

"""


class Solution:
    def isWordInRow(self, word, row):
        for ch in word:
            if ch not in row:
                return False
        return True

    def findWords(self, words: List[str]) -> List[str]:
        keyboardRows = [set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")]
        answer  =[]

        for word in words:
            row = None
            currentWord = word.lower()
            if currentWord[0] in keyboardRows[0]:
                row = 0
            elif currentWord[0] in keyboardRows[1]:
                row = 1
            elif currentWord[0] in keyboardRows[2]:
                row = 2
            
            if row is not None and self.isWordInRow(currentWord[1:], keyboardRows[row]):
                answer.append(word)

        return answer