class Solution:
    def sortVowels(self, s: str) -> str:
        nonIncreasingVowels = ["u", "o", "i", "e", "a", "U", "O", "I", "E", "A"]
        vowels = set(nonIncreasingVowels)
        # Hashmap of vowels and their count
        vowelsLookup = {}
        for ch in s:
            if ch in vowels:
                if ch not in vowelsLookup:
                    vowelsLookup[ch] = 0
                vowelsLookup[ch] += 1

        sortedVowels = [None] * len(s)
        for i in range(len(s)):
            # If s[i] is a vowel then it should be replaced by a vowel such that if follows non decreasing order
            if s[i] in vowelsLookup:
                # Check the correct vowel to replace. If the last vowel in nonIncreasingVowels is present in vowelsLookup than use it else search for next potential vowel.
                vowelToReplace = nonIncreasingVowels[-1]
                while vowelToReplace not in vowelsLookup or vowelsLookup[vowelToReplace] < 1:
                    nonIncreasingVowels.pop()
                    vowelToReplace = nonIncreasingVowels[-1]
                # Replace the correct vowel
                sortedVowels[i] = vowelToReplace
                vowelsLookup[vowelToReplace] -= 1
            else:
                sortedVowels[i] = s[i]
        return "".join(sortedVowels)