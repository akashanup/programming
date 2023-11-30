class Solution:
    KNIGHT_MOVES = {
        -1: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        0: [4, 6],
        1: [6, 8],
        2: [7, 9],
        3: [4, 8],
        4: [0, 3, 9],
        5: [],
        6: [0, 1, 7],
        7: [2, 6],
        8: [1, 3],
        9: [2, 4]
    }
    MOD = (10 ** 9) + 7

    def __recur(self, n, prevCell, lookup):
        if n == 0:
            return 1
        if (n, prevCell) not in lookup:
            count = 0
            for cell in Solution.KNIGHT_MOVES[prevCell]:
                count += self.__recur(n - 1, cell, lookup)
            lookup[(n, prevCell)] = count
        return lookup[(n, prevCell)] % Solution.MOD

    def knightDialer(self, n: int) -> int:
        return self.__recur(n, -1, {})

