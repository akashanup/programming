class Solution:
    def originalDigits(self, s: str) -> str:
        # 0 -> 2 -> 4 -> 6 -> 8 -> 1 -> 3 -> 5 ->7 -> 9
        digitEnglishMap = {
            0: {"z": 1, "e": 1, "r": 1, "o": 1},
            1: {"o": 1, "n": 1, "e": 1},
            2: {"t": 1, "w": 1, "o": 1},
            3: {"t": 1, "h": 1, "r": 1, "e": 2},
            4: {"f": 1, "o": 1, "u": 1, "r": 1},
            5: {"f": 1, "i": 1, "v": 1, "e": 1},
            6: {"s": 1, "i": 1, "x": 1},
            7: {"s": 1, "e": 2, "v": 1, "n": 1},
            8: {"e": 1, "i": 1, "g": 1, "h": 1, "t": 1},
            9: {"n": 2, "i": 1, "e": 1}
        }
        lookup = {}
        for ch in s:
            if ch not in lookup:
                lookup[ch] = 0
            lookup[ch] += 1

        ans = []
        """
        Stream is taken in this order because digits which has some unique chars should be processed first so that
        it doesn't get overriden.
        
        Example:
        s: "zeroonetwothreefourfivesixseveneightnine"
        incase of strem(0-9) 01113356 which is wrong.
        correct output: "0123456789"
        """
        for digit in (0, 2, 4, 6, 8, 1, 3, 5, 7, 9):
            digitExists = True
            while digitExists:
                # Check whether digit exists
                for ch in digitEnglishMap[digit]:
                    count = digitEnglishMap[digit][ch]
                    if ch not in lookup or lookup[ch] < count:
                        digitExists = False
                        break
                # If digit exists, add it in ans and remove from lookup
                if digitExists:
                    ans.append(str(digit))
                    for ch in digitEnglishMap[digit]:
                        count = digitEnglishMap[digit][ch]
                        lookup[ch] -= count
        return "".join(sorted(ans))