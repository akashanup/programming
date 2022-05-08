class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        words = set(dictionary)

        sentence = sentence.split(' ')

        for i, word in enumerate(sentence):
            for j in range(1, len(word)):
                if word[:j] in words:
                    sentence[i] = word[:j]
                    break

        return ' '.join(sentence)
