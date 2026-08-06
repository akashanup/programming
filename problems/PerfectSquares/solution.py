class Solution:
    def numSquares(self, n: int) -> int:
        squareRootN = int(n ** (1/2))
        if (squareRootN ** 2) == n:
            return 1
        nums = [1]
        for i in range(2, squareRootN + 1):
            nums.append(i ** 2)
        currentLevel = [0]
        level = 0
        while True:
            nextLevel = []
            for i in currentLevel:
                for j in nums:
                    if i + j == n:
                        return level + 1
                    elif i + j < n:
                        nextLevel.append(i + j)
            level += 1
            # Remove duplicates
            currentLevel = list(set(nextLevel))


# print(Solution().numSquares(15))
print(Solution().numSquares(71268))
