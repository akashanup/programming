class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        chunks = []
        lastIndex = -1
        n = len(dominoes)
        # Split the dominoes in chunks
        for i in range(n):
            if dominoes[i] == 'L':
                chunks.append(dominoes[lastIndex+1:i+1])
                lastIndex = i
        if lastIndex < n - 1:
            chunks.append(dominoes[lastIndex+1:n])
        finalDominoes = ''
        for chunk in chunks:
            chunkLen = len(chunk)
            if chunk[-1] == 'L':
                if 'R' in chunk:
                    startIndexR = chunk.index('R')
                    endIndexR = chunk.rindex('R')
                    # Values for start pointer can never have 'L' because of the above split.
                    finalDominoes += '.' * startIndexR
                    finalDominoes += 'R' * (endIndexR - startIndexR)
                    start = endIndexR
                    end = chunkLen - 1
                    if (end - start) % 2:
                        halfLen = ((end - start) // 2) + 1
                        finalDominoes += ('R' * halfLen) + ('L' * halfLen)
                    else:
                        halfLen = (end - start) // 2
                        finalDominoes += ('R' * halfLen) + '.' + ('L' * halfLen)
                else:
                    finalDominoes += 'L' * chunkLen
            else:
                if 'R' in chunk:
                    indexR = chunk.index('R')
                    finalDominoes += ('.' * indexR) + ('R' * (chunkLen - indexR))
                else:
                    finalDominoes += '.' * chunkLen
        return finalDominoes
