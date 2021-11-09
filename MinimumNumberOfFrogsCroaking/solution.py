class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        hash = {
            'c': croakOfFrogs.count('c'),
            'r': croakOfFrogs.count('r'),
            'o': croakOfFrogs.count('o'),
            'a': croakOfFrogs.count('a'),
            'k': croakOfFrogs.count('k'),
        }

        """
            Check whether the given string is a valid combination 'croaks'
            If the count of any of 'c', r', 'o', 'a', 'k' is different then it is invalid.
            
        """
        if hash['c'] != hash['r'] or hash['r'] != hash['o'] or hash['o'] != hash['a'] or hash['a'] != hash['k']:
            return -1

        maxFrogs = 0
        frogs = 0

        """
            If we encounter a 'c' while iterating croakOfFrogs then it means a frog has started croaking. So frogs += 1
            If we encounter a 'k' while iterating croakOfFrogs then it means a frog has finished croaking. So frogs -= 1
        """

        for char in croakOfFrogs:
            hash[char] -= 1
            if char == 'c':
                frogs += 1
                maxFrogs = max(maxFrogs, frogs)
            elif char == 'k':
                frogs -= 1
            else:
                """
                    If at any point the below condition holds true then it is an invalid string because the sequence 'c','r','o','a','k' would break.
                """
                if not (hash['c'] <= hash['r'] <= hash['o'] <= hash['a'] <= hash['k']):
                    return -1
        return maxFrogs

