class Solution:
    """
        For n length vowel permutations:-
        1. Loop through the vowels
        2. For the first index(i.e, lastChar is None) fill it with the vowels
        3. For all the subsequent indexes, fill the values from the followedBy list of chosen vowel(i.e, followedBy[lastChar])
        4. Repeat/Recur Step 3 till n == 0. If n becomes zero then it means that we have made a valid string of n length so return 1.
    """
    vowels = ["a", "e", "i", "o", "u"]
    followedBy = {"a": ["e"], "e": ["a", "i"], "i": ["a", "e", "o", "u"], "o": ["u", "i"], "u": ["a"]}

    def dp(self, n, lastChar, lookup):
        if n == 0:
            return 1
        key = (n, lastChar)
        if key not in lookup:
            permutations = 0
            if not lastChar:
                for char in self.vowels:
                    permutations += self.dp(n-1, char, lookup)
            else:
                for char in self.followedBy[lastChar]:
                    permutations += self.dp(n-1, char, lookup)
            lookup[key] = permutations
        return lookup[key] % ((10 ** 9) + 7)

    def countVowelPermutation(self, n: int) -> int:
        return self.dp(n, None, {})
